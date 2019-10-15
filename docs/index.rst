Sphinx Verilog Diagrams
=======================

Single DFF
----------

Verilog Code
~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. literalinclude:: verilog/dff.v
      :language: verilog

Result
++++++

.. literalinclude:: verilog/dff.v
   :language: verilog

Yosys BlackBox Diagram
~~~~~~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: yosys-bb

Result
++++++

.. verilog-diagram:: verilog/dff.v
   :type: yosys-bb


Yosys AIG Diagram
~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: yosys-aig

Result
++++++

.. verilog-diagram:: verilog/dff.v
   :type: yosys-aig

NetlistSVG Diagram
~~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/dff.v
      :type: netlistsvg

Result
++++++

.. verilog-diagram:: verilog/dff.v
   :type: netlistsvg

Combinational Full Adder
------------------------

Verilog Code
~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. literalinclude:: verilog/adder.v
      :language: verilog


Result
++++++

.. literalinclude:: verilog/adder.v
   :language: verilog

Yosys BlackBox Diagram
~~~~~~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: yosys-bb
      :module: ADDER

Result
++++++

.. verilog-diagram:: verilog/adder.v
   :type: yosys-bb
   :module: ADDER


Yosys AIG Diagram
~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: yosys-aig
      :module: ADDER

Result
++++++

.. verilog-diagram:: verilog/adder.v
   :type: yosys-aig
   :module: ADDER


NetlistSVG Diagram
~~~~~~~~~~~~~~~~~~

RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:
   :emphasize-lines: 2

   .. verilog-diagram:: verilog/adder.v
      :type: netlistsvg
      :module: ADDER


Result
++++++

.. verilog-diagram:: verilog/adder.v
   :type: netlistsvg
   :module: ADDER

NetlistSVG Demos
----------------

CARRY4 Bits
~~~~~~~~~~~

Verilog Code
++++++++++++

.. literalinclude:: verilog/carry4-bits.v
   :language: verilog


RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/carry4-bits.v
      :type: netlistsvg
      :module: CARRY4
      :caption: carry4-bits.v

Result
++++++

.. verilog-diagram:: verilog/carry4-bits.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-bits.v


CARRY4 Whole
~~~~~~~~~~~~

Verilog Code
++++++++++++

.. literalinclude:: verilog/carry4-whole.v
   :language: verilog


RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/carry4-whole.v
      :type: netlistsvg
      :module: CARRY4
      :caption: carry4-whole.v

Result
++++++

.. verilog-diagram:: verilog/carry4-whole.v
   :type: netlistsvg
   :module: CARRY4
   :caption: carry4-whole.v

MUXCY Example
~~~~~~~~~~~~~

Verilog Code
++++++++++++

.. literalinclude:: verilog/muxcy.v
   :language: verilog


RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/muxcy.v
      :type: netlistsvg
      :caption: muxcy.v
      :module: MUXCY

Result
++++++

.. verilog-diagram:: verilog/muxcy.v
   :type: netlistsvg
   :caption: muxcy.v
   :module: MUXCY

XORCY Example
~~~~~~~~~~~~~

Verilog Code
++++++++++++

.. literalinclude:: verilog/xorcy.v
   :language: verilog


RST Directive
+++++++++++++

.. code-block:: rst
   :linenos:

   .. verilog-diagram:: verilog/xorcy.v
      :type: netlistsvg
      :caption: xorcy.v
      :module: XORCY

Result
++++++

.. verilog-diagram:: verilog/xorcy.v
   :type: netlistsvg
   :caption: xorcy.v
   :module: XORCY
