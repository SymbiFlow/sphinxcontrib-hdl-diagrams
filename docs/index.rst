Sphinx Verilog Diagrams
=======================

sphinx-verilog-diagrams is an extension to Sphinx to make it easier to write
nice documentation from Verilog files.

You use the |verilog-diagram|_ RST directive to generate various styles of
diagrams from verilog code.

Most of the time there will be a license header at the top of source code, 
which we might not want to show in the documentation. 
This extension also provides the |no-license|_ RST directive which works exactly 
like the `.. literalinclude` directive, but the `lines` option is overridden
to only show the lines after the license header.


.. |verilog-diagram| replace:: `.. verilog-diagram`
.. _verilog-diagram: #usage
.. |no-license| replace:: `.. no-license`
.. _no-license: #verilog-code-block-without-license-header

The project repository is hosted on `GitHub <https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams>`_.

Installation
------------

Python 3.5+ is required.

.. code-block:: bash

   pip install sphinxcontrib-verilog-diagrams

Or,

.. code-block:: bash

   python3 -m pip install sphinxcontrib-verilog-diagrams

Sphinx integration
~~~~~~~~~~~~~~~~~~

In your conf.py, add the following lines.

.. code-block:: python

   extensions = [
      ...,
      'sphinxcontrib_verilog_diagrams',
   ]

Non-python dependencies
~~~~~~~~~~~~~~~~~~~~~~~
These dependencies can either be installed on your system or you can install them using the
conda `environment.yml <https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams/blob/master/environment.yml>`_ file.

- `yosys <https://github.com/YosysHQ/yosys>`_ (required)
- `netlistsvg <https://github.com/nturley/netlistsvg>`_ (optional)

Usage
-----

The `verilog-diagram` RST directive can be used to generate a diagram from Verilog code and include it in your documentation.

.. code-block:: rst

   .. verilog-diagram:: file.v
      :type: XXXXX
      :module: XXXX
      :flatten:

Options
~~~~~~~

`:type:` - Verilog Diagram Types;

- `yosys-blackbox` - Netlist rendered by Yosys.
- `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
- `netlistsvg` - Render output with `netlistsvg <https://github.com/nturley/netlistsvg>`_

`:module:` - Which module to diagram.

`:flatten:` - Use the Yosys `flatten` command before generating the image.

Examples
--------

Single DFF
~~~~~~~~~~

Verilog Code Block (with license header)
++++++++++++++++++++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. literalinclude:: verilog/dff.v
      :language: verilog
      :linenos:
      :caption: verilog/dff.v

Result
******

.. literalinclude:: verilog/dff.v
   :language: verilog
   :linenos:
   :caption: verilog/dff.v

Verilog Code Block (without license header)
++++++++++++++++++++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. no-license:: verilog/dff.v
      :language: verilog
      :linenos:
      :caption: verilog/dff.v

Result
******

.. no-license:: verilog/dff.v
   :language: verilog
   :linenos:
   :caption: verilog/dff.v


Yosys BlackBox Diagram
++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: yosys-bb

Result
******

.. verilog-diagram:: verilog/dff.v
   :type: yosys-bb


Yosys AIG Diagram
+++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: yosys-aig

Result
******

.. verilog-diagram:: verilog/dff.v
   :type: yosys-aig


NetlistSVG Diagram
++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: netlistsvg

Result
******

.. verilog-diagram:: verilog/dff.v
   :type: netlistsvg


Combinational Full Adder
~~~~~~~~~~~~~~~~~~~~~~~~

Verilog Code
++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. no-license:: verilog/adder.v
      :language: verilog
      :linenos:
      :caption: verilog/adder.v


Result
******

.. no-license:: verilog/adder.v
   :language: verilog
   :linenos:
   :caption: verilog/adder.v


Yosys BlackBox Diagram
++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: yosys-bb
      :module: ADDER

Result
******

.. verilog-diagram:: verilog/adder.v
   :type: yosys-bb
   :module: ADDER


Yosys AIG Diagram
+++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: yosys-aig
      :module: ADDER

Result
******

.. verilog-diagram:: verilog/adder.v
   :type: yosys-aig
   :module: ADDER


NetlistSVG Diagram
+++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: netlistsvg
      :module: ADDER


Result
******

.. verilog-diagram:: verilog/adder.v
   :type: netlistsvg
   :module: ADDER

NetlistSVG Demos
~~~~~~~~~~~~~~~~


CARRY4 defined directly
+++++++++++++++++++++++

.. no-license:: verilog/carry4-whole.v
   :language: verilog
   :linenos:
   :caption: verilog/carry4-whole.v

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/carry4-whole.v
      :type: netlistsvg
      :module: CARRY4
      :caption: carry4-whole.v

.. verilog-diagram:: verilog/carry4-whole.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-whole.v


CARRY4 defined by components
++++++++++++++++++++++++++++

.. no-license:: verilog/carry4-bits.v
   :language: verilog
   :linenos:
   :caption: verilog/carry4-bits.v


.. no-license:: verilog/muxcy.v
   :language: verilog
   :linenos:
   :caption: verilog/muxcy.v


.. no-license:: verilog/xorcy.v
   :language: verilog
   :linenos:
   :caption: verilog/xorcy.v


MUXCY
*****

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/muxcy.v
      :type: netlistsvg
      :caption: muxcy.v
      :module: MUXCY


.. verilog-diagram:: verilog/muxcy.v
   :type: netlistsvg
   :caption: muxcy.v
   :module: MUXCY


XORCY
*****

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/xorcy.v
      :type: netlistsvg
      :caption: xorcy.v
      :module: XORCY


.. verilog-diagram:: verilog/xorcy.v
   :type: netlistsvg
   :caption: xorcy.v
   :module: XORCY

CARRY4 without flatten
**********************

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/carry4-bits.v
      :type: netlistsvg
      :module: CARRY4
      :caption: carry4-bits.v without flatten


.. verilog-diagram:: verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-bits.v without flatten

CARRY4 with flatten
*******************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 4

   .. verilog-diagram:: verilog/carry4-bits.v
      :type: netlistsvg
      :module: CARRY4
      :flatten:
      :caption: carry4-bits.v with flatten


.. verilog-diagram:: verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :flatten:
   :caption: carry4-bits.v with flatten

