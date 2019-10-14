Sphinx Verilog Diagrams
=======================

Single DFF
----------

.. literalinclude:: verilog/dff.v
   :language: verilog

Yosys BlackBox Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/dff.v
   :type: yosys-bb

Yosys AIG Diagram
~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/dff.v
   :type: yosys-aig

NetlistSVG Diagram
~~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/dff.v
   :type: netlistsvg

Combinational Full Adder
------------------------

.. literalinclude:: verilog/adder.v
   :language: verilog

Yosys BlackBox Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/adder.v
   :type: yosys-bb
   :module: ADDER


Yosys AIG Diagram
~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/adder.v
   :type: yosys-aig
   :module: ADDER


NetlistSVG Diagram
~~~~~~~~~~~~~~~~~~

.. verilog-diagram:: verilog/adder.v
   :type: netlistsvg
   :module: ADDER


NetlistSVG Demos
----------------

.. verilog-diagram:: verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-bits.v


.. verilog-diagram:: verilog/carry4-whole.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-whole.v


.. verilog-diagram:: verilog/muxcy.v
   :type: netlistsvg
   :caption: muxcy.v
   :module: MUXCY


.. verilog-diagram:: verilog/xorcy.v
   :type: netlistsvg
   :caption: xorcy.v
   :module: XORCY


