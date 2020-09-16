Test Yosys Script Option
========================

This test checks whether the global and per diagram custom yosys script setting
works as intended.

Yosys Blackbox Diagram
----------------------

The following examples are related to the Yosys BlackBox diagram.
The same checks are provided for Yosys-AIG diagrams and Netlistsvg diagrams.
There are presented in the next sections of this file.

Global script test
++++++++++++++++++

The global Yosys script setting is achieved by placing
the ``verilog_diagram_yosys_script`` variable in the ``conf.py`` script.

Here is the fragment of the ``conf.py`` script::

    verilog_diagram_yosys_script = os.path.realpath('yosys_script.ys')

The following ``hdl-diagram`` diagram should be placed in an RST file::

   .. hdl-diagram:: adder.v
      :type: yosys-blackbox
      :module: ADDER

Below you can see the output of the directive:

.. hdl-diagram:: adder.v
   :type: yosys-blackbox
   :module: ADDER

.. note:: Since the commands used in the custom scripts do not modify the design,
  the custom script usage will be visible in the sphinx build log.

Script per diagram
++++++++++++++++++

Per diagram Yosys script setting is achieved by using the ``:yosys_script:``
option with the ``hdl-diagram`` directive.

Here is the example of a ``hdl-diagram`` directive that should be
placed in an RST file::

   .. hdl-diagram:: adder.v
      :type: yosys-blackbox
      :module: ADDER
      :yosys_script: yosys_script2.ys

Below you can see the output of the directive:

.. hdl-diagram:: adder.v
   :type: yosys-blackbox
   :module: ADDER
   :yosys_script: yosys_script2.ys

.. note:: Since the Yosys ommands used in the custom scripts do not modify
   the design, the custom script usage will be visible in the sphinx build log.

Global overwrite
++++++++++++++++

It is possible to overwrite the global Yosys script setting using
the ``:yosys_script:`` option. To reset the setting to the default value,
you can use the ``:yosys_script: default`` setting.

Here is an example of a ``hdl-diagram`` directive that should be
placed in an RST file::

   .. hdl-diagram:: adder.v
      :type: yosys-blackbox
      :module: ADDER
      :yosys_script: default

Below you can see the output of the directive:

.. hdl-diagram:: adder.v
   :type: yosys-blackbox
   :module: ADDER
   :yosys_script: default

.. note:: Since the Yosys commands used in the custom scripts do not modify
   the design, the custom script usage will be visible in the sphinx build log.

Yosys Blackbox Diagram
----------------------

Global script test
++++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: yosys-aig
      :module: ADDER

.. hdl-diagram:: adder.v
   :type: yosys-aig
   :module: ADDER

Script per diagram
++++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: yosys-aig
      :module: ADDER
      :yosys_script: yosys_script2.ys

.. hdl-diagram:: adder.v
   :type: yosys-aig
   :module: ADDER
   :yosys_script: yosys_script2.ys

Global overwrite
++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: yosys-aig
      :module: ADDER
      :yosys_script: default

.. hdl-diagram:: adder.v
   :type: yosys-aig
   :module: ADDER
   :yosys_script: default


Netlistsvg diagram
------------------

Global script test
++++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER
      :yosys_script: default

.. hdl-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
   :yosys_script: default

Script per diagram
++++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER
      :yosys_script: default

.. hdl-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
   :yosys_script: default

Global overwrite
++++++++++++++++

.. code-block:: rst

   .. hdl-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER
      :yosys_script: default

.. hdl-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
   :yosys_script: default

