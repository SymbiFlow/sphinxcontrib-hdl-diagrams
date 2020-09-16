Test Yowasp - yowasp
====================

This test checks whether the ability to switch between different Yosys types
works as intended. This functionality is enabled by ``verilog_domain_yosys``
variable, which can take the following values:

- ``yowasp`` (default)
- ``system``
- ``<path-to-yosys>``

The diagrams presented below have been generated using the ``<yowasp>`` option.

Here is the fragment of the ``conf.py`` script, used to configure the extension::

   verilog_diagram_yosys = 'yowasp'

.. note:: ``yowasp`` is the default setting. The configuration presented above can be omitted.

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
