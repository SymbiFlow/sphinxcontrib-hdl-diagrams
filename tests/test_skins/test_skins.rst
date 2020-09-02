Test Skin Option
================

This test checks whether the global and per diagram skin setting work as intended.

Global Skin Option Setting
--------------------------

The global skin setting is achieved by setting the ``verilog_diagram_skin``
variable in the ``conf.py`` script.

Here is the fragment of the ``conf.py`` script::

   verilog_diagram_skin = os.path.realpath('skin-purple.svg')

The following ``verilog-diagram`` diagram should be placed in an RST file::

   .. verilog-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER

Below you can see the output of the directive. The diagram presented below
should be black-purple.

.. verilog-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER

Per Diagram Skin Setting
------------------------

Per diagram skin setting is achieved by using the ``:skin:`` option with
the ``verilog-diagram`` directive.

The following ``verilog-diagram`` directive should be placed in an RST file::

   .. verilog-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER
      :skin: skin-yellow.svg

.. verilog-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
   :skin: skin-yellow.svg

Below you can see the output of the directive. The diagram presented below
should be black-yellow.

Overwrite the Global Skin Setting
---------------------------------

It is possible to overwrite the global skin settings using the ``:skin:`` option.
To reset the skin setting to the default value, you can use the ``:skin: default``
setting.

The following ``verilog-diagram`` directive should be placed in an RST file::

   .. verilog-diagram:: adder.v
      :type: netlistsvg
      :module: ADDER
      :skin: default

Below you can see the output of the directive. The diagram presented below
should be black-white.

.. verilog-diagram:: adder.v
   :type: netlistsvg
   :module: ADDER
   :skin: default
