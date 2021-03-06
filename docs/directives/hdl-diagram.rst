hdl-diagram
===========

The `hdl-diagram` RST directive can be used to generate a diagram from HDL code and include it in your documentation.

.. code-block:: rst

   .. hdl-diagram:: file.v
      :type: XXXXX
      :module: XXXX
      :flatten:

.. note::

   The `verilog-diagram` directive is kept as an alias of this directive for 
   compatibility purposes.

Options
-------

`:type:` - Verilog Diagram Types;

- `yosys-blackbox` - Netlist rendered by Yosys.
- `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
- `netlistsvg` - Render output with `netlistsvg <https://github.com/nturley/netlistsvg>`_

`:module:` - Which module to diagram.

`:flatten:` - Use the Yosys `flatten` command before generating the image.

Input Formats
-------------
This directive supports 3 input formats: Verilog code, nMigen code, and RTLIL.

Verilog
+++++++

.. no-license:: ../code/verilog/counter.v
   :language: verilog
   :linenos:

.. code-block:: rst
   :linenos:
   :emphasize-lines: 1

   .. hdl-diagram:: ../code/verilog/counter.v
      :type: netlistsvg

.. hdl-diagram:: ../code/verilog/counter.v
   :type: netlistsvg


nMigen
++++++

.. no-license:: ../code/nmigen/counter.py
   :language: python
   :linenos:
   :emphasize-lines: 5,17,18

.. code-block:: rst
   :linenos:
   :emphasize-lines: 1

   .. hdl-diagram:: ../code/nmigen/counter.py
      :type: netlistsvg

.. hdl-diagram:: ../code/nmigen/counter.py
   :type: netlistsvg

.. note::

   As `hdl-diagram` expects the nMigen script to write RTLIL code to stdout,
   make sure to include the following lines of code.

   .. code-block:: py
      :linenos:

      from nmigen.back import rtlil
      print(rtlil.convert(..., ports=[...]))


RTLIL
+++++

.. no-license:: ../code/rtlil/counter.il
   :language: text
   :linenos:

.. code-block:: rst
   :linenos:
   :emphasize-lines: 1

   .. hdl-diagram:: ../code/rtlil/counter.il
      :type: netlistsvg

.. hdl-diagram:: ../code/rtlil/counter.il
   :type: netlistsvg


Diagram Types
-------------

Yosys BlackBox Diagram
++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/dff.v
      :type: yosys-bb

Result
******

.. hdl-diagram:: ../code/verilog/dff.v
   :type: yosys-bb


Yosys AIG Diagram
+++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/dff.v
      :type: yosys-aig

Result
******

.. hdl-diagram:: ../code/verilog/dff.v
   :type: yosys-aig


NetlistSVG Diagram
++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/dff.v
      :type: netlistsvg

Result
******

.. hdl-diagram:: ../code/verilog/dff.v
   :type: netlistsvg