Test Compatibility Package
==========================

This test checks whether the ``sphinxcontrib-verilog-diagrams`` compatibility
package works as intended.

Here is the fragment of the ``conf.py`` script, used to configure the extension::

   extensions = [
       'sphinxcontrib_verilog_diagrams',
   ]

Yosys BlackBox Diagram
----------------------

.. code-block:: rst

   .. verilog-diagram:: adder.v
      :type: yosys-blackbox
      :module: ADDER

.. verilog-diagram:: adder.v
   :type: yosys-blackbox
   :module: ADDER

Yosys AIG Diagram
-----------------

.. code-block:: rst

   .. verilog-diagram:: adder.v
      :type: yosys-aig
      :module: ADDER

.. verilog-diagram:: adder.v
   :type: yosys-aig
   :module: ADDER

Netlistsvg Diagram
------------------

.. code-block:: rst

   .. verilog-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER

.. verilog-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
