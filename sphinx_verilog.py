#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import re
import sys
import subprocess

import docutils
from docutils import statemachine, nodes, io, utils
from docutils.parsers import rst
from docutils.core import ErrorString
from docutils.utils import SafeString, column_width

import sphinx
from sphinx.errors import SphinxError
from sphinx.locale import _, __
from sphinx.util import logging
from sphinx.util.i18n import search_image_for_language
from sphinx.util.osutil import ensuredir, ENOENT, EPIPE, EINVAL

if False:
    # For type annotation
    from typing import Any, Dict, List, Tuple  # NOQA
    from sphinx.application import Sphinx  # NOQA

logger = logging.getLogger(__name__)


class VerilogDiagramError(SphinxError):
    category = 'VerilogDiagram error'


class verilog_diagram(nodes.General, nodes.Inline, nodes.Element):
    '''Base class for verilog_diagram node'''
    pass


class VerilogDiagram(rst.Directive):
    """Directive class to include diagram generated from Verilog.

    """
    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        'type': str,
        'module': str,
        'flatten': bool,
    }

    def run(self):
        """Most of this method is from ``docutils.parser.rst.Directive``.

        docutils version: 0.12
        """
        if not self.state.document.settings.file_insertion_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)

        print("-->", dir(self.state_machine))
        env = self.state.document.settings.env

        # Pass
        # ------
        fname = '%s-%s.%s' % (prefix, name, format)
        relfn = posixpath.join(self.builder.imgpath, fname)
        outfn = path.join(self.builder.outdir, self.builder.imagedir, fname)
        # ------

        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))

        verilog_path = rst.directives.path(self.arguments[0])
        verilog_path = os.path.normpath(os.path.join(source_dir, verilog_path))
        verilog_path = utils.relative_path(None, verilog_path)
        verilog_path = nodes.reprunicode(verilog_path)

        # get options (currently not use directive-specific options)
        encoding = self.options.get(
            'encoding', self.state.document.settings.input_encoding)
        e_handler = self.state.document.settings.input_encoding_error_handler

        # open the including file
        self.state.document.settings.record_dependencies.add(verilog_path)
        if not os.path.exists(verilog_path):
            raise self.severe('File "%s" not found\n' % (SafeString(verilog_path),))

        srcpath, srclineno = self.state_machine.get_source_and_line()
        srcdir, srcfile = os.path.split(srcpath)
        srcbase, srcext = os.path.splitext(srcfile)

        verilog_path_segments = [verilog_path]
        while verilog_path_segments[0]:
            a, b = os.path.split(verilog_path_segments[0])
            verilog_path_segments[0:1] = [a, b]

        verilog_file, verilog_ext = os.path.splitext(verilog_path_segments[-1])

        opath = os.path.join(srcdir, '-'.join(
            [srcbase, str(srclineno)] +
            verilog_path_segments[1:-1] +
            [verilog_file]))

        #    include_file = io.FileInput(source_path=path,
        #                                encoding=encoding,
        #                                error_handler=e_handler)

        flatten = self.options.get('flatten', False)
        module = self.options.get('module', 'top')
        diagram_type = self.options.get('type', 'netlistsvg')

        if diagram_type.startswith('yosys'):
            assert diagram_type.startswith('yosys-'), diagram_type
            self.diagram_yosys(
                verilog_path, opath, module=module, flatten=flatten)
        elif diagram_type == 'netlistsvg':
            self.diagram_netlistsvg(
                verilog_path, opath, module=module, flatten=flatten)
        else:
            raise self.severe('Invalid diagram type "%s"\n' %
                              (SafeString(diagram_type),))

        config = self.state.document.settings.env.config
        #include_lines = statemachine.string2lines(converter(rawtext),
        #                                          tab_width,
        #                                          convert_whitespace=True)
        #self.state_machine.insert_input(include_lines, path)
        return []

    def run_yosys(self, src, cmd):
        ycmd = "yosys -p '{cmd}' {src}".format(src=src, cmd=cmd),
        subprocess.check_output(ycmd, shell=True)

    def diagram_yosys(self, ipath, opath, module='top', flatten=False):
        if flatten:
            flatten = '-flatten'
        else:
            flatten = ''

        ofile = opath + '.svg'
        if os.path.exists(ofile):
            #print('Output file exists: {}'.format(ofile))
            os.remove(ofile)

        self.run_yosys(
            src=ipath,
            cmd = """\
prep -top {top} {flatten}; show -format svg -prefix {opath} {top}
""".format(top=module, flatten=flatten, opath=opath).strip())

        assert os.path.exists(ofile), 'Output file {} was not created!'.format(ofile)
        print('Output file created: {}'.format(ofile))

    def diagram_netlistsvg(self, ipath, opath, module='top', flatten=False):
        print('netlistsvg', ipath, opath, module, flatten)
        if flatten:
            flatten = '-flatten'
        else:
            flatten = ''

        ojson = opath + '.json'
        if os.path.exists(ojson):
            os.remove(ojson)

        self.run_yosys(
            src=ipath,
            cmd = """\
prep -top {top} {flatten}; cd {top}; write_json {opath}.json
""".format(top=module, flatten=flatten, opath=opath).strip())
        assert os.path.exists(ojson), 'Output file {} was not created!'.format(ojson)
        print('Output file created: {}'.format(ojson))


def render_symbol_html(
        self, node, code, options, prefix='symbol', imgcls=None, alt=None):
    # type: (nodes.NodeVisitor, verilog_diagram, unicode, Dict, unicode, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA
    format = self.builder.config.verilog_diagram_output_format
    try:
        if format not in ('png', 'svg'):
            raise SymbolatorError("verilog_diagram_output_format must be one of 'png', "
                                "'svg', but is %r" % format)
        fname, outfn = render_symbol(self, code, options, format, prefix)
    except SymbolatorError as exc:
        logger.warning('verilog_diagram code %r: ' % code + str(exc))
        raise nodes.SkipNode

    if fname is None:
        self.body.append(self.encode(code))
    else:
        if alt is None:
            alt = node.get('alt', self.encode(code).strip())
        imgcss = imgcls and 'class="%s"' % imgcls or ''
        if format == 'svg':
            svgtag = '''<object data="%s" type="image/svg+xml">
            <p class="warning">%s</p></object>\n''' % (fname, alt)
            self.body.append(svgtag)
        else:
            if 'align' in node:
                self.body.append('<div align="%s" class="align-%s">' %
                                 (node['align'], node['align']))
            self.body.append('<img src="%s" alt="%s" %s/>\n' %
                             (fname, alt, imgcss))
            if 'align' in node:
                self.body.append('</div>\n')

    raise nodes.SkipNode



def html_visit_verilog_diagram(self, node):
    # type: (nodes.NodeVisitor, verilog_diagram) -> None
    render_symbol_html(self, node, node['code'], node['options'])


def setup(app):
    """When used for sphinx extension."""
    # type: (Sphinx) -> Dict[unicode, Any]

    try:
        yosys_path = subprocess.check_output('which yosys', shell=True)
        print("Yosys found at {}".format(yosys_path))
    except subprocess.CalledProcessError as e:
        #app.severe('Yosys not found! {}'.format(e))
        raise docutils.ApplicationError('Yosys not found ({})'.format(e))

    app.add_node(
        verilog_diagram,
        html=(html_visit_verilog_diagram, None),
    )

    app.add_directive('verilog-diagram', VerilogDiagram)
    metadata = dict(
        version="0.0",
        parallel_read_safe=True,
        parallel_write_safe=True,
    )

    app.add_config_value('verilog_diagram_output_format', 'svg', 'html')


    return metadata
