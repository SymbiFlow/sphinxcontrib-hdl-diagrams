Combinational Full Adder
========================

Verilog Code
++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. no-license:: ../code/verilog/adder.v
      :language: verilog
      :linenos:


Result
******

.. no-license:: ../code/verilog/adder.v
   :language: verilog
   :linenos:


Yosys BlackBox Diagram
++++++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/adder.v
      :type: yosys-bb
      :module: ADDER

Result
******

.. hdl-diagram:: ../code/verilog/adder.v
   :type: yosys-bb
   :module: ADDER


Yosys AIG Diagram
+++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/adder.v
      :type: yosys-aig
      :module: ADDER

Result
******

.. hdl-diagram:: ../code/verilog/adder.v
   :type: yosys-aig
   :module: ADDER


NetlistSVG Diagram
++++++++++++++++++

RST Directive
*************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. hdl-diagram:: ../code/verilog/adder.v
      :type: netlistsvg
      :module: ADDER


Result
******

.. hdl-diagram:: ../code/verilog/adder.v
   :type: netlistsvg
   :module: ADDER

NetlistSVG Demos
~~~~~~~~~~~~~~~~


CARRY4 defined directly
+++++++++++++++++++++++

.. no-license:: ../code/verilog/carry4-whole.v
   :language: verilog
   :linenos:

.. code-block:: rst
   :linenos:

   .. hdl-diagram:: ../code/verilog/carry4-whole.v
      :type: netlistsvg
      :module: CARRY4

.. hdl-diagram:: ../code/verilog/carry4-whole.v
   :type: netlistsvg
   :module: CARRY4


CARRY4 defined by components
++++++++++++++++++++++++++++

.. no-license:: ../code/verilog/carry4-bits.v
   :language: verilog
   :linenos:


.. no-license:: ../code/verilog/muxcy.v
   :language: verilog
   :linenos:


.. no-license:: ../code/verilog/xorcy.v
   :language: verilog
   :linenos:


MUXCY
*****

.. code-block:: rst
   :linenos:

   .. hdl-diagram:: ../code/verilog/muxcy.v
      :type: netlistsvg
      :caption: muxcy.v
      :module: MUXCY


.. hdl-diagram:: ../code/verilog/muxcy.v
   :type: netlistsvg
   :caption: muxcy.v
   :module: MUXCY


XORCY
*****

.. code-block:: rst
   :linenos:

   .. hdl-diagram:: ../code/verilog/xorcy.v
      :type: netlistsvg
      :caption: xorcy.v
      :module: XORCY


.. hdl-diagram:: ../code/verilog/xorcy.v
   :type: netlistsvg
   :caption: xorcy.v
   :module: XORCY

CARRY4 without flatten
**********************

.. code-block:: rst
   :linenos:

   .. hdl-diagram:: ../code/verilog/carry4-bits.v
      :type: netlistsvg
      :module: CARRY4
      :caption: carry4-bits.v without flatten


.. hdl-diagram:: ../code/verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-bits.v without flatten

CARRY4 with flatten
*******************

.. code-block:: rst
   :linenos:
   :emphasize-lines: 4

   .. hdl-diagram:: ../code/verilog/carry4-bits.v
      :type: netlistsvg
      :module: CARRY4
      :flatten:
      :caption: carry4-bits.v with flatten


.. hdl-diagram:: ../code/verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :flatten:
   :caption: carry4-bits.v with flatten