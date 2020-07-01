hdl-diagram
===========

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

.. code-block:: rst
   :linenos:
   :emphasize-lines: 1

   .. hdl-diagram:: ../code/nmigen/counter.py
      :type: netlistsvg

.. hdl-diagram:: ../code/nmigen/counter.py
   :type: netlistsvg


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