#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import re
import sys
from argparse import ArgumentParser, Namespace

from docutils import statemachine, nodes, io, utils
from docutils.parsers import rst
from docutils.core import ErrorString
from docutils.utils import SafeString, column_width


class MdInclude(rst.Directive):
    """Directive class to include diagram generated from Verilog.

    """
    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        'type': str,
        'flatten': bool,
    }

    def run(self):
        """Most of this method is from ``docutils.parser.rst.Directive``.

        docutils version: 0.12
        """
        if not self.state.document.settings.file_insertion_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)
        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))
        path = rst.directives.path(self.arguments[0])
        path = os.path.normpath(os.path.join(source_dir, path))
        path = utils.relative_path(None, path)
        path = nodes.reprunicode(path)

        # get options (currently not use directive-specific options)
        encoding = self.options.get(
            'encoding', self.state.document.settings.input_encoding)
        e_handler = self.state.document.settings.input_encoding_error_handler
        tab_width = self.options.get(
            'tab-width', self.state.document.settings.tab_width)

        # open the including file
        try:
            self.state.document.settings.record_dependencies.add(path)
            include_file = io.FileInput(source_path=path,
                                        encoding=encoding,
                                        error_handler=e_handler)
        except UnicodeEncodeError:
            raise self.severe('Problems with "%s" directive path:\n'
                              'Cannot encode input file path "%s" '
                              '(wrong locale?).' %
                              (self.name, SafeString(path)))
        except IOError as error:
            raise self.severe('Problems with "%s" directive path:\n%s.' %
                              (self.name, ErrorString(error)))

        flatten = self.options.get('flatten', False)
        diagram_type = self.options.get('type', 'netlistsvg')
        try:
            rawtext = include_file.read()
        except UnicodeError as error:
            raise self.severe('Problem with "%s" directive:\n%s' %
                              (self.name, ErrorString(error)))

        config = self.state.document.settings.env.config
        include_lines = statemachine.string2lines(converter(rawtext),
                                                  tab_width,
                                                  convert_whitespace=True)
        self.state_machine.insert_input(include_lines, path)
        return []


def setup(app):
    """When used for sphinx extension."""
    global _is_sphinx
    _is_sphinx = True
    app.add_directive('mdinclude', MdInclude)
    metadata = dict(
        version=__version__,
        parallel_read_safe=True,
        parallel_write_safe=True,
    )
    return metadata
