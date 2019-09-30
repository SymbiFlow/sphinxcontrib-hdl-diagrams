#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    name='sphinx-verilog',
    version='0.0',
    description='Generate diagrams from Verilog in Sphinx.',
    long_description=readme,
    author="Tim 'mithro' Ansell",
    author_email='me@mith.ro',
    url='https://github.com/mithro/sphinx-verilog-diagrams',
    py_modules=['sphinx_verilog'],
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
