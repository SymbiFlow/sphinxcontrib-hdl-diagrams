#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020  The SymbiFlow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

"""
sphinx_hdl_diagrams
~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import re
import codecs
import posixpath
import subprocess
import sys

from os import path

from docutils import statemachine, nodes, io, utils
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import ViewList

import sphinx
from sphinx.directives.code import LiteralInclude
from sphinx.errors import SphinxError
from sphinx.locale import _, __
from sphinx.util import logging
from sphinx.util.i18n import search_image_for_language
from sphinx.util.osutil import ensuredir, ENOENT, EPIPE, EINVAL

if False:
    # For type annotation
    from typing import Any, Dict, List, Tuple  # NOQA
    from sphinx.application import Sphinx  # NOQA


try:
    from .version import __version__
except ImportError:
    __version__ = "0.0.dev0"


logger = logging.getLogger(__name__)


class HDLDiagramError(SphinxError):
    category = 'HDLDiagram error'


class hdl_diagram(nodes.General, nodes.Inline, nodes.Element):
    '''Base class for hdl_diagram node'''
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


def hdl_diagram_name(srcpath, srclineno, hdl_path):
    srcdir, srcfile = path.split(srcpath)
    srcbase, srcext = path.splitext(srcfile)

    hdl_path = path.normpath(path.join(srcdir, hdl_path))
    hdl_path = utils.relative_path(None, hdl_path)
    hdl_path = nodes.reprunicode(hdl_path)

    hdl_path_segments = [hdl_path]
    while hdl_path_segments[0]:
        a, b = path.split(hdl_path_segments[0])
        hdl_path_segments[0:1] = [a, b]

    hdl_file, hdl_ext = path.splitext(hdl_path_segments[-1])

    return '-'.join(
        [srcbase, str(srclineno)] +
        hdl_path_segments[1:-1] +
        [hdl_file],
    )


class NoLicenseInclude(LiteralInclude):
    def run(self):
        # type: () -> List[nodes.Node]

        rel_filename, filename = self.env.relfn2path(self.arguments[0])
        code = open(filename, 'r').read().strip().split('\n')

        first_line = next(
            (idx for idx, line in enumerate(code) if 'SPDX' in line), 1)
        if first_line > 1:
            first_line += 3 if code[first_line][1] == '*' else 2
        last_line = len(code)

        while len(code[first_line - 1]) == 0:
            first_line += 1

        self.options['lines'] = '{}-{}'.format(first_line, last_line)
        self.options['lineno-start'] = first_line

        try:
            return LiteralInclude.run(self)
        except Exception as exc:
            return [document.reporter.warning(exc, line=self.lineno)]


class HDLDiagram(Directive):
    """
    Directive to insert diagram generated from HDL code.
    """

    has_content = True

    required_arguments = 1
    optional_arguments = 1

    final_argument_whitespace = False

    option_spec = {
        'type': str,
        'module': str,
        'flatten': bool,
        'skin': str,
        'yosys_script': str,

        'alt': directives.unchanged,
        'align': align_spec,
        'caption': directives.unchanged,
    }

    global_variable_options = {
        "verilog_diagram_output_format": ["svg", "png"],
        "verilog_diagram_skin": ["default"],  # or path
        "verilog_diagram_yosys_script": ["default"],  # or path
        "verilog_diagram_yosys": ["yowasp", "system"]  # or path
    }

    def run(self):
        # type: () -> List[nodes.Node]

        if not self.state.document.settings.file_insertion_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)

        print("hdl-diagram", self)

        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)

        if self.arguments:
            hdl_file = self.arguments[0]

            outname = hdl_diagram_name(
                *self.state_machine.get_source_and_line(), hdl_file)

            # self.state.document.settings.record_dependencies.add(hdl_path)

            env = self.state.document.settings.env
            argument = search_image_for_language(hdl_file, env)
            rel_filename, filename = env.relfn2path(hdl_file)
            env.note_dependency(rel_filename)
        else:
            assert False, "TODO!"
            # TODO: ????
            hdl_diagram_code = '\n'.join(self.content)

        node = hdl_diagram()
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

        yosys_script = self.options.get('yosys_script', None)
        if yosys_script not in [None, 'default']:
            _, yosys_script_filename = env.relfn2path(yosys_script)
            if not path.exists(yosys_script_filename):
                raise VerilogDiagramError("Yosys script {} does not exist!".format(yosys_script_filename))
            else:
                node['options']['yosys_script'] = yosys_script_filename
        else:
            node['options']['yosys_script'] = yosys_script

        skin = self.options.get('skin', None)
        if skin not in [None, 'default']:
            _, skin_filename = env.relfn2path(skin)
            if not os.path.exists(skin_filename):
                raise VerilogDiagramError("Skin file {} does not exist!".format(skin_filename))
            else:
                node['options']['skin'] = skin_filename
        else:
            node['options']['skin'] = skin

        caption = self.options.get('caption')
        if caption:
            node = figure_wrapper(self, node, caption)

        self.add_name(node)
        return [node]


def run_yosys(src, cmd, yosys='yowasp'):
    if yosys == 'yowasp':
        import yowasp_yosys
        ycmd = ["-q", "-p", "{}".format(cmd), src]
        print("Running YoWASP yosys: {}".format(ycmd))
        yowasp_yosys.run_yosys(ycmd)
    elif yosys == 'system':
        ycmd = "yosys -p '{cmd}' {src}".format(src=src, cmd=cmd)
        print("Running yosys: {}".format(ycmd))
        subprocess.check_output(ycmd, shell=True)
    else:
        ycmd = "{yosys} -p '{cmd}' {src}".format(yosys=yosys, src=src, cmd=cmd)
        print("Running yosys: {}".format(ycmd))
        subprocess.check_output(ycmd, shell=True)


def diagram_yosys(ipath, opath, module='top', flatten=False,
                  yosys_script='default', yosys='yowasp'):

    # Assertions

    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)
    yosys_options = VerilogDiagram.global_variable_options["verilog_diagram_yosys"]
    assert yosys in yosys_options or os.path.exists(yosys), "Invalid verilog_diagram_yosys value!"
    if yosys_script != 'default':
        assert path.exists(yosys_script), 'Yosys script file missing: {}'.format(yosys_script)
    oprefix, oext = path.splitext(opath)
    assert oext.startswith('.'), oext

    # Diagram generation

    oext = oext[1:]

    if flatten:
        flatten = '-flatten'
    else:
        flatten = ''

    if yosys_script == 'default':
        yosys_script_cmd = ""
    else:
        yosys_script_cmd = "script {}".format(yosys_script)

    yosys_cmd = "prep -top {top} {flatten}; cd {top}; {script}; show -format {fmt} -prefix {oprefix}".format(
        top=module,
        flatten=flatten,
        fmt=oext,
        oprefix=oprefix,
        script=yosys_script_cmd
    ).strip()
    run_yosys(ipath, yosys_cmd, yosys)

    if yosys == 'yowasp':
        # somehow yowasp_yosys fails to execute `dot` to convert the dot file to svg,
        # which works on native yosys, perhaps a limitation with wasm
        svgdata = subprocess.check_output(["dot", "-Tsvg", "{}.dot".format(oprefix)])
        with open("{}.svg".format(oprefix), "wb") as img:
            img.write(svgdata)

    assert path.exists(opath), 'Output file {} was not created!'.format(oopath)
    print('Output file created: {}'.format(opath))

def run_netlistsvg(ipath, opath, skin='default'):
    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)
    if skin != 'default':
        assert path.exists(skin), 'Skin file missing: {}'.format(skin)

    netlistsvg_cmd = "netlistsvg {ipath} -o {opath}".format(ipath=ipath, opath=opath)
    if skin != 'default':
        netlistsvg_cmd += " --skin {skin}".format(skin=skin)

    print("Running netlistsvg:", netlistsvg_cmd)
    subprocess.check_output(netlistsvg_cmd, shell=True)

    assert path.exists(opath), 'Output file {} was not created!'.format(opath)
    print('netlistsvg - Output file created: {}'.format(opath))


def diagram_netlistsvg(ipath, opath, module='top', flatten=False,
                       yosys_script='default', skin='default', yosys='yowasp'):
    # Assertions

    assert path.exists(ipath), 'Input file missing: {}'.format(ipath)
    assert not path.exists(opath), 'Output file exists: {}'.format(opath)
    yosys_options = VerilogDiagram.global_variable_options["verilog_diagram_yosys"]
    assert yosys in yosys_options or os.path.exists(yosys), "Invalid verilog_diagram_yosys value!"
    if yosys_script != 'default':
        assert path.exists(yosys_script), 'Yosys script file missing: {}'.format(yosys_script)
    if skin != 'default':
        assert path.exists(skin), 'Skin file missing: {}'.format(skin)
    oprefix, oext = path.splitext(opath)
    assert oext.startswith('.'), oext

    # Diagram generation

    oext = oext[1:]

    if flatten:
        flatten = '-flatten'
    else:
        flatten = ''

    if yosys_script == 'default':
        yosys_script_cmd = ""
    else:
        yosys_script_cmd = "script {}".format(yosys_script)

    ojson = oprefix + '.json'
    if path.exists(ojson):
        os.remove(ojson)

    yosys_cmd = """prep -top {top} {flatten}; cd {top}; {script}; write_json {compat} {ojson}""".format(
        top=module,
        flatten=flatten,
        ojson=ojson,
        script=yosys_script_cmd,
        compat="-compat-int" if yosys == 'yowasp' else ""
    ).strip()
    run_yosys(ipath, yosys_cmd, yosys)
    assert path.exists(ojson), 'Output file {} was not created!'.format(ojson)

    run_netlistsvg(ojson, opath, skin)
    print('netlistsvg - Output file created: {}'.format(ojson))


def nmigen_to_rtlil(fname, oname):
    subprocess.run([sys.executable, fname], stdout=open(oname, "w"),
                    shell=False, check=True)


def render_diagram(self, code, options, format, skin, yosys_script):
    # type: (nodes.NodeVisitor, unicode, Dict, unicode, unicode) -> Tuple[unicode, unicode]
    """Render hdl code into a PNG or SVG output file."""

    source_path = code
    source_fn, source_ext = os.path.splitext(source_path)

    fname = '%s.%s' % (options['outname'], format)
    relfn = posixpath.join(self.builder.imgpath, fname)
    outfn = path.join(self.builder.outdir, self.builder.imagedir, fname)

    if source_ext == '.py':
        module = 'top'
        ilfn = path.join(self.builder.outdir, self.builder.imagedir, options['outname'] + '.il')
        nmigen_to_rtlil(source_path, ilfn)
        source_path = ilfn
    elif source_ext == '.il' or source_ext == '.v':
        module = options['module']
    else:
        raise HDLDiagramError("hdl_diagram_code file extension must be one of '.v', "
                            "'.il', or '.py', but is %r" % source_ext)

    if path.isfile(outfn):
        print('Exiting file:', outfn)
        return relfn, outfn

    ensuredir(path.dirname(outfn))

    yosys_script = options['yosys_script'] if options['yosys_script'] is not None else yosys_script
    skin = options['skin'] if options['skin'] is not None else skin

    yosys = self.builder.config.verilog_diagram_yosys
    yosys_options = VerilogDiagram.global_variable_options["verilog_diagram_yosys"]
    if yosys not in yosys_options and not os.path.exists(yosys):
        raise VerilogDiagramError("Yosys not found!")
    else:
        yosys = yosys if yosys in yosys_options else os.path.realpath(yosys)

    diagram_type = options['type']
    if diagram_type.startswith('yosys'):
        assert diagram_type.startswith('yosys-'), diagram_type
        diagram_yosys(
            verilog_path,
            outfn,
            module=options['module'],
            flatten=options['flatten'],
            yosys_script=yosys_script,
            yosys=yosys)
    elif diagram_type == 'netlistsvg':
        diagram_netlistsvg(
            verilog_path,
            outfn,
            module=options['module'],
            flatten=options['flatten'],
            skin=skin,
            yosys=yosys)
    else:
        raise Exception('Invalid diagram type "%s"' % diagram_type)
        #raise self.severe(\n' %
        #                  (SafeString(diagram_type),))

    return relfn, outfn


def render_diagram_html(
        self, node, code, options, imgcls=None, alt=None):
    # type: (nodes.NodeVisitor, hdl_diagram, unicode, Dict, unicode, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA

    yosys_script = self.builder.config.verilog_diagram_yosys_script
    if yosys_script != 'default' and not path.exists(yosys_script):
        raise VerilogDiagramError("Yosys script file {} does not exist! Change verilog_diagram_yosys_script variable".format(yosys_script))

    skin = self.builder.config.verilog_diagram_skin
    if skin != 'default' and not path.exists(skin):
        raise VerilogDiagramError("Skin file {} does not exist! Change verilog_diagram_skin variable".format(skin))

    format = self.builder.config.verilog_diagram_output_format
    try:
        if format not in ('png', 'svg'):
            raise HDLDiagramError("hdl_diagram_output_format must be one of 'png', "
                                "'svg', but is %r" % format)
        fname, outfn = render_diagram(self, code, options, format, skin, yosys_script)
    except HDLDiagramError as exc:
        logger.warning('hdl_diagram code %r: ' % code + str(exc))
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


def html_visit_hdl_diagram(self, node):
    # type: (nodes.NodeVisitor, hdl_diagram) -> None
    render_diagram_html(self, node, node['code'], node['options'])


def render_diagram_latex(self, node, code, options):
    # type: (nodes.NodeVisitor, hdl_diagram, unicode, Dict, unicode) -> None

    try:
        fname, outfn = render_diagram(self, code, options, 'pdf')
    except HDLDiagramError as exc:
        logger.warning('hdl_diagram code %r: ' % code + str(exc))
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


def latex_visit_hdl_diagram(self, node):
    # type: (nodes.NodeVisitor, hdl_diagram) -> None
    render_diagram_latex(self, node, node['code'], node['options'])


def render_diagram_texinfo(self, node, code, options):
    # type: (nodes.NodeVisitor, hdl_diagram, unicode, Dict, unicode) -> None
    try:
        fname, outfn = render_diagram(self, code, options, 'png')
    except HDLDiagramError as exc:
        logger.warning('hdl_diagram code %r: ' % code + str(exc))
        raise nodes.SkipNode
    if fname is not None:
        self.body.append('@image{%s,,,[hdl_diagram],png}\n' % fname[:-4])
    raise nodes.SkipNode


def texinfo_visit_hdl_diagram(self, node):
    # type: (nodes.NodeVisitor, hdl_diagram) -> None
    render_diagram_texinfo(self, node, node['code'], node['options'])


def text_visit_hdl_diagram(self, node):
    # type: (nodes.NodeVisitor, hdl_diagram) -> None
    if 'alt' in node.attributes:
        self.add_text(_('[diagram: %s]') % node['alt'])
    else:
        self.add_text(_('[diagram]'))
    raise nodes.SkipNode


def man_visit_hdl_diagram(self, node):
    # type: (nodes.NodeVisitor, hdl_diagram) -> None
    if 'alt' in node.attributes:
        self.body.append(_('[diagram: %s]') % node['alt'])
    else:
        self.body.append(_('[diagram]'))
    raise nodes.SkipNode


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_node(hdl_diagram,
                 html=(html_visit_hdl_diagram, None),
                 latex=(latex_visit_hdl_diagram, None),
                 texinfo=(texinfo_visit_hdl_diagram, None),
                 text=(text_visit_hdl_diagram, None),
                 man=(man_visit_hdl_diagram, None))
    app.add_directive('hdl-diagram', HDLDiagram)
    app.add_directive('no-license', NoLicenseInclude)
    app.add_config_value('hdl_diagram_output_format', 'svg', 'html')
    app.add_config_value('hdl_diagram_skin', 'default', 'html')
    app.add_config_value('hdl_diagram_yosys_script', 'default', 'html')
    app.add_config_value('hdl_diagram_yosys', 'yowasp', 'html')
    return {'version': '1.0', 'parallel_read_safe': True}
