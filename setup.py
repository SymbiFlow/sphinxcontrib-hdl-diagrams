#!/usr/bin/env python
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

import sys
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.md')
with open(readme_file) as f:
    readme = f.read()

install_requires = ['docutils']

setup(
    name='sphinxcontrib-verilog-diagrams',
    version='0.0',
    description='Generate diagrams from Verilog in Sphinx.',
    long_description=readme,
    author="Tim 'mithro' Ansell",
    author_email='me@mith.ro',
    url='https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams',
    py_modules=['sphinxcontrib_verilog_diagrams'],
    license="Apache 2.0",
    keywords='Verilog sphinx sphinx-extension netlistsvg FPGA',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    install_requires=install_requires,
)
