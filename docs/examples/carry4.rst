CARRY4 example for Series 7 FPGA
================================

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