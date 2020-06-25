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

from setuptools import setup, find_packages

__dir__ = path.dirname(path.abspath(__file__))

# Manually import the version number so dependencies don't need to be installed
# when running setup.py
version_file = path.join(__dir__, "sphinxcontrib_verilog_diagrams", "version.py")
if path.exists(version_file):
    exec(open(version_file).read())
else:
    __version__ = "0.0.dev0"

readme_file = path.join(__dir__, 'README.rst')
try:
    with open(readme_file) as f:
        readme = f.read()
except FileNotFoundError as e:
    import traceback
    traceback.print_exc()
    readme = ''
    __version__ = 'error'

install_requires = [
    'setuptools',
    'docutils',
    'sphinx',
]

setup(
    name='sphinxcontrib-verilog-diagrams',
    version=__version__,
    description='Generate diagrams from Verilog in Sphinx.',
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="The SymbiFlow Authors",
    author_email='symbiflow@lists.librecores.org',
    url='https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams',
    packages=find_packages(),
    license="Apache 2.0",
    keywords='Verilog sphinx sphinx-extension netlistsvg FPGA',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: Apache 2.0',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    install_requires=install_requires,
)
