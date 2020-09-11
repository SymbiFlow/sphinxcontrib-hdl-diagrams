Test Yowasp - path
==================

This test checks whether the ability to switch between different Yosys types
works as intended. This functionality is enabled by ``verilog_domain_yosys``
variable, which can take the following values:

- ``yowasp`` (default)
- ``system``
- ``<path-to-yosys>``

The diagrams presented below have been generated using the ``<path-to-yosys>`` option.

Here is the fragment of the ``conf.py`` script, used to configure the extension:

.. literalinclude:: conf.py
   :lines: 58

Yosys BlackBox Diagram
----------------------

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: yosys-blackbox
      :module: ADDER

.. hdl-diagram:: adder.v
   :type: yosys-blackbox
   :module: ADDER

Yosys AIG Diagram
-----------------

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: yosys-aig
      :module: ADDER

.. hdl-diagram:: adder.v
   :type: yosys-aig
   :module: ADDER

Netlistsvg Diagram
------------------

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER

.. hdl-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
