#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier:	ISC

"""
sphinx_verilog_diagrams
~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import re
import codecs
import posixpath
import subprocess

from os import path

from docutils import statemachine, nodes, io, utils
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import ViewList

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


def figure_wrapper(directive, node, caption):
    # type: (Directive, nodes.Node, unicode) -> nodes.figure
    figure_node = nodes.figure('', node)
    if 'align' in node:
        figure_node['align'] = node.attributes.pop('align')

    parsed = nodes.Element()
    directive.state.nested_parse(
        ViewList([caption], source=''), directive.content_offset, parsed)
    caption_node = nodes.caption(
        parsed[0].rawsource, '', *parsed[0].children)
    caption_node.source = parsed[0].source
    caption_node.line = parsed[0].line
    figure_node += caption_node
    return figure_node


def align_spec(argument):
    # type: (Any) -> bool
    return directives.choice(argument, ('left', 'center', 'right'))


def verilog_diagram_name(srcpath, srclineno, verilog_path):
    srcdir, srcfile = path.split(srcpath)
    srcbase, srcext = path.splitext(srcfile)

    verilog_path = path.normpath(path.join(srcdir, verilog_path))
    verilog_path = utils.relative_path(None, verilog_path)
    verilog_path = nodes.reprunicode(verilog_path)

    verilog_path_segments = [verilog_path]
    while verilog_path_segments[0]:
        a, b = path.split(verilog_path_segments[0])
        verilog_path_segments[0:1] = [a, b]

    verilog_file, verilog_ext = path.splitext(verilog_path_segments[-1])

    return '-'.join(
        [srcbase, str(srclineno)] +
        verilog_path_segments[1:-1] +
        [verilog_file],
    )


class VerilogDiagram(Directive):
    """
    Directive to insert diagram generated from Verilog code.
    """

    has_content = True

    required_arguments = 1
    optional_arguments = 1

    final_argument_whitespace = False

    option_spec = {
        'type': str,
        'module': str,
        'flatten': bool,

        'alt': directives.unchanged,
        'align': align_spec,
        'caption': directives.unchanged,
    }

    def run(self):
        # type: () -> List[nodes.Node]

        if not self.state.document.settings.file_insertion_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)

        print("verilog-diagram", self)

        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)

        if self.arguments:
            verilog_file = self.arguments[0]

            outname = verilog_diagram_name(
                *self.state_machine.get_source_and_line(), verilog_file)

            # self.state.document.settings.record_dependencies.add(verilog_path)

            env = self.state.document.settings.env
            argument = search_image_for_language(verilog_file, env)
            rel_filename, filename = env.relfn2path(verilog_file)
            env.note_dependency(rel_filename)
        else:
            assert False, "TODO!"
            # TODO: ????
            verilog_diagram_code = '\n'.join(self.content)

        node = verilog_diagram()
        node['code'] = filename
        node['options'] = {}
        node['options']['outname'] = outname
        node['options']['flatten'] = 'flatten' in self.options
        node['options']['module'] = self.options.get('module', 'top')
        node['options']['type'] = self.options.get('type', 'netlistsvg')

        if 'alt' in self.options:
            node['alt'] = self.options['alt']
        if 'align' in self.options:
            node['align'] = self.options['align']

        caption = self.options.get('caption')
        if caption:
            node = figure_wrapper(self, node, caption)

        self.add_name(node)
        return [node]


def run_yosys(src, cmd):
    ycmd = "yosys -p '{cmd}' {src}".format(src=src, cmd=cmd)
    print("Running yosys:", ycmd)
    subprocess.check_output(ycmd, shell=True)


def diagram_yosys(ipath, opath, module='top', flatten=False):
    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)
    oprefix, oext = path.splitext(opath)
    assert oext.startswith('.'), oext
    oext = oext[1:]

    if flatten:
        flatten = '-flatten'
    else:
        flatten = ''

    run_yosys(
        src=ipath,
        cmd = """\
prep -top {top} {flatten}; cd {top}; show -format {fmt} -prefix {oprefix}
""".format(top=module, flatten=flatten, fmt=oext, oprefix=oprefix).strip(),
    )

    assert path.exists(opath), 'Output file {} was not created!'.format(oopath)
    print('Output file created: {}'.format(opath))


def run_netlistsvg(ipath, opath, skin=None):
    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)

    netlistsvg_cmd = "netlistsvg {ipath} -o {opath}".format(ipath=ipath, opath=opath)
    if skin:
        netlistsvg_cmd += " --skin {skin}".format(skin=skin)
    subprocess.check_output(netlistsvg_cmd, shell=True)

    assert path.exists(opath), 'Output file {} was not created!'.format(opath)
    print('netlistsvg - Output file created: {}'.format(opath))


def diagram_netlistsvg(ipath, opath, module='top', flatten=False):
    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)
    oprefix, oext = path.splitext(opath)
    assert oext.startswith('.'), oext
    oext = oext[1:]

    if flatten:
        flatten = '-flatten'
    else:
        flatten = ''

    ojson = oprefix + '.json'
    if path.exists(ojson):
        os.remove(ojson)

    run_yosys(
        src=ipath,
        cmd = """\
prep -top {top} {flatten}; cd {top}; write_json -compat-int {ojson}
""".format(top=module, flatten=flatten, ojson=ojson).strip())
    assert path.exists(ojson), 'Output file {} was not created!'.format(ojson)

    run_netlistsvg(ojson, opath)
    print('netlistsvg - Output file created: {}'.format(ojson))


def render_diagram(self, code, options, format):
    # type: (nodes.NodeVisitor, unicode, Dict, unicode, unicode) -> Tuple[unicode, unicode]
    """Render verilog_diagram code into a PNG or SVG output file."""

    verilog_path = code

    fname = '%s.%s' % (options['outname'], format)
    relfn = posixpath.join(self.builder.imgpath, fname)
    outfn = path.join(self.builder.outdir, self.builder.imagedir, fname)

    if path.isfile(outfn):
        print('Exiting file:', outfn)
        return relfn, outfn

    ensuredir(path.dirname(outfn))

    diagram_type = options['type']
    if diagram_type.startswith('yosys'):
        assert diagram_type.startswith('yosys-'), diagram_type
        diagram_yosys(
            verilog_path, outfn, module=options['module'], flatten=options['flatten'])
    elif diagram_type == 'netlistsvg':
        diagram_netlistsvg(
            verilog_path, outfn, module=options['module'], flatten=options['flatten'])
    else:
        raise Exception('Invalid diagram type "%s"' % diagram_type)
        #raise self.severe(\n' %
        #                  (SafeString(diagram_type),))

    return relfn, outfn


def render_diagram_html(
        self, node, code, options, imgcls=None, alt=None):
    # type: (nodes.NodeVisitor, verilog_diagram, unicode, Dict, unicode, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA
    format = self.builder.config.verilog_diagram_output_format

    try:
        if format not in ('png', 'svg'):
            raise VerilogDiagramError("verilog_diagram_output_format must be one of 'png', "
                                "'svg', but is %r" % format)
        fname, outfn = render_diagram(self, code, options, format)
    except VerilogDiagramError as exc:
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
    render_diagram_html(self, node, node['code'], node['options'])


def render_diagram_latex(self, node, code, options):
    # type: (nodes.NodeVisitor, verilog_diagram, unicode, Dict, unicode) -> None

    try:
        fname, outfn = render_diagram(self, code, options, 'pdf')
    except VerilogDiagramError as exc:
        logger.warning('verilog_diagram code %r: ' % code + str(exc))
        raise nodes.SkipNode

    is_inline = self.is_inline(node)
    if is_inline:
        para_separator = ''
    else:
        para_separator = '\n'

    if fname is not None:
        post = None  # type: unicode
        if not is_inline and 'align' in node:
            if node['align'] == 'left':
                self.body.append('{')
                post = '\\hspace*{\\fill}}'
            elif node['align'] == 'right':
                self.body.append('{\\hspace*{\\fill}')
                post = '}'
        self.body.append('%s\\includegraphics{%s}%s' %
                         (para_separator, fname, para_separator))
        if post:
            self.body.append(post)

    raise nodes.SkipNode


def latex_visit_verilog_diagram(self, node):
    # type: (nodes.NodeVisitor, verilog_diagram) -> None
    render_diagram_latex(self, node, node['code'], node['options'])


def render_diagram_texinfo(self, node, code, options):
    # type: (nodes.NodeVisitor, verilog_diagram, unicode, Dict, unicode) -> None
    try:
        fname, outfn = render_diagram(self, code, options, 'png')
    except VerilogDiagramError as exc:
        logger.warning('verilog_diagram code %r: ' % code + str(exc))
        raise nodes.SkipNode
    if fname is not None:
        self.body.append('@image{%s,,,[verilog_diagram],png}\n' % fname[:-4])
    raise nodes.SkipNode


def texinfo_visit_verilog_diagram(self, node):
    # type: (nodes.NodeVisitor, verilog_diagram) -> None
    render_diagram_texinfo(self, node, node['code'], node['options'])


def text_visit_verilog_diagram(self, node):
    # type: (nodes.NodeVisitor, verilog_diagram) -> None
    if 'alt' in node.attributes:
        self.add_text(_('[diagram: %s]') % node['alt'])
    else:
        self.add_text(_('[diagram]'))
    raise nodes.SkipNode


def man_visit_verilog_diagram(self, node):
    # type: (nodes.NodeVisitor, verilog_diagram) -> None
    if 'alt' in node.attributes:
        self.body.append(_('[diagram: %s]') % node['alt'])
    else:
        self.body.append(_('[diagram]'))
    raise nodes.SkipNode


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_node(verilog_diagram,
                 html=(html_visit_verilog_diagram, None),
                 latex=(latex_visit_verilog_diagram, None),
                 texinfo=(texinfo_visit_verilog_diagram, None),
                 text=(text_visit_verilog_diagram, None),
                 man=(man_visit_verilog_diagram, None))
    app.add_directive('verilog-diagram', VerilogDiagram)
    app.add_config_value('verilog_diagram_output_format', 'svg', 'html')
    return {'version': '1.0', 'parallel_read_safe': True}

