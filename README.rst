sphinxcontrib-verilog-diagrams
==============================


.. image:: https://img.shields.io/pypi/v/sphinxcontrib-verilog-diagrams.svg
   :target: https://pypi.python.org/pypi/sphinxcontrib-verilog-diagrams
   :alt: PyPI


.. image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-verilog-diagrams.svg
   :target: https://pypi.python.org/pypi/sphinxcontrib-verilog-diagrams
   :alt: PyPI version


.. image:: https://readthedocs.org/projects/sphinxcontrib-verilog-diagrams/badge
   :target: https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest/
   :alt: Documentation


.. image:: https://travis-ci.com/SymbiFlow/sphinxcontrib-verilog-diagrams.svg?branch=master
   :target: https://travis-ci.com/SymbiFlow/sphinxcontrib-verilog-diagrams
   :alt: Build Status


.. image:: https://codecov.io/gh/SymbiFlow/sphinxcontrib-verilog-diagrams/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/SymbiFlow/sphinxcontrib-verilog-diagrams
   :alt: codecov


----

Sphinx Extension which generates various types of diagrams from Verilog code.

`sphinxcontrib-verilog-diagrams <https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams>`_
is a Sphinx extension to make it easier to write nice documentation from
Verilog files. It primarily uses `Yosys <https://github.com/YosysHQ/yosys>`_ to do the Verilog reading.

Check out the `documentation <https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest>`_ for examples.

Installation
------------

Python 3.5+ is required.

.. code-block::

   pip install sphinxcontrib-verilog-diagrams

Or,

.. code-block::

   python3 -m pip install sphinxcontrib-verilog-diagrams

Sphinx Integration
^^^^^^^^^^^^^^^^^^

In your conf.py, add the following lines.

.. code-block:: python

   extensions = [
       ...,
       'sphinxcontrib_verilog_diagrams',
   ]

Non-Python Dependencies
^^^^^^^^^^^^^^^^^^^^^^^

These dependencies can be either installed on your system or install using the
conda ``environment.yml`` file with;

.. code-block:: bash

   conda XXXX

Required
~~~~~~~~

* |yosys|_
.. |yosys| replace:: `yosys`
.. _yosys: https://github.com/YosysHQ/yosys

Optional
~~~~~~~~

* |netlistsvg|_
.. |netlistsvg| replace:: `netlistsvg`
.. _netlistsvg: https://github.com/nturley/netlistsvg

Usage
-----

``verilog-diagram``
^^^^^^^^^^^^^^^^^^^

The ``verilog-diagram`` RST directive can be used to generate a diagram from Verilog code and include it in your documentation.
Check out the `examples <https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest/>`_ to see how to use it.

.. code-block:: rst


   .. verilog-diagram:: file.v
      :type: XXXXX
      :module: XXXX
      :flatten:

Options
~~~~~~~

``:type:`` - Verilog Diagram Types;


* ``yosys-blackbox`` - Netlist rendered by Yosys.
* ``yosys-aig`` - Verilog file run through ``aigmap`` before image is generated directly in Yosys.
* ``netlistsvg`` - Render output with `netlistsvg <https://github.com/nturley/netlistsvg>`_

``:module:`` - Which module to diagram.

``:flatten:`` - Use the Yosys ``flatten`` command before generating the image.

Example
~~~~~~~

Here is a diagram of a 4-bit carry chain.


.. image:: ./carry4-flatten.svg
   :target: ./carry4-flatten.svg
   :alt: 4-bit carry chain


``no-license``
^^^^^^^^^^^^^^

This extension also provides the ``no-license`` directive which can be used to include code blocks from a file, but omitting the license header
at the top of the file. It behaves like the ``literalinclude`` directive, but the ``lines`` option is overridden to only show the lines after the license header.

.. code-block:: rst


   .. no-license:: verilog/dff.v
      :language: verilog
      :linenos:
      :caption: verilog/dff.v

Example
~~~~~~~

Here is a comparison between the ``literalinclude`` and ``no-license`` directives.

.. code-block:: rst

   .. literalinclude:: verilog/dff.v
      :language: verilog
      :caption: verilog/dff.v

.. code-block:: verilog

   /*
    * Copyright (C) 2020  The SymbiFlow Authors.
    *
    * Licensed under the Apache License, Version 2.0 (the "License");
    * you may not use this file except in compliance with the License.
    * You may obtain a copy of the License at
    *
    *     https://www.apache.org/licenses/LICENSE-2.0
    *
    * Unless required by applicable law or agreed to in writing, software
    * distributed under the License is distributed on an "AS IS" BASIS,
    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    * See the License for the specific language governing permissions and
    * limitations under the License.
    *
    * SPDX-License-Identifier: Apache-2.0
    */

   // Single flip-flip test.
   module top(input clk, input di, output do);
     always @( posedge clk )
       do <= di;
   endmodule // top

.. code-block:: rst

   .. no-license:: verilog/dff.v
      :language: verilog
      :caption: verilog/dff.v

.. code-block:: verilog

   // Single flip-flip test.
   module top(input clk, input di, output do);
     always @( posedge clk )
       do <= di;
   endmodule // top

Licence
-------

`Apache 2.0 <LICENSE>`_
