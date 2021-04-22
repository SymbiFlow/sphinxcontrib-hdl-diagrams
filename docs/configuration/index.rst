Configuration
=============

This is the list of possible configurations that go in ``conf.py``.

Yosys
+++++

``hdl_diagram_yosys`` tells the program what version or binary of Yosys to use.
By default it is set to ``YoWASP``. Setting it to ``system``, the program will
use Yosys available in the current PATH. It can also contain the path to a specific
Yosys binary.::

    hdl_diagram_yosys = "yowasp" # default

    hdl_diagram_yosys = "system" # use yosys from PATH

    hdl_diagram_yosys = "<path-to-Yosys>" # use specific yosys binary


netlistsvg
++++++++++

netlistsvg can take various skin files for use when creating diagrams. It is
set to ``default`` by default, using the built-in netlistsvg skin.::

    hdl_diagram_skin = "<path-to-skin>"


Output format
+++++++++++++

The output format for the generated diagrams can either be set to ``svg`` or ``png``.::

    hdl_diagram_output_format = "svg"

    hdl_diagram_output_format = "png"


GHDL
++++

ghdl-yosys-plugin can either be built into Yosys or loaded at runtime. If it is built into Yosys,
then set this configuration option to ``built-in``. If it is loaded at runtime, then this can
either be set to ``module`` if the shared library is located at ``YOSYS_PREFIX/share/yosys/plugins/
ghdl.so``, or as a path to the ``ghdl.so`` shared library. ::

    hdl_diagram_ghdl = "built-in" # default, if ghdl-yosys-plugin is built into Yosys

    hdl_diagram_ghdl = "module" # passes `-m ghdl` to Yosys

    hdl_diagram_ghdl = "<path-to-GHDL-shared-library>" # path to specific ghdl.so,
                                                       # passes `-m '<path>'` to Yosys

The VHDL standard used for GHDL can be set globally using this configuration option.::

    hdl_diagram_ghdl_std = "08" # default, for VHDL 2008

    hdl_diagram_ghdl_std = "97" # for VHDL 1993

Common Errors
+++++++++++++

.. code-block::

    ERROR:
      This version of Yosys cannot load plugins at runtime.
      Some plugins may have been included at build time.
      Use option `-H' to see the available built-in and plugin commands.

This error signifies that the current version of Yosys cannot load plugins
at runtime, and so all plugins must be prebuit. For VHDL, ``hdl_diagram_ghdl``
must be set to ``built-in``.

.. code-block::

    ERROR: Can't guess frontend for input file `' (missing -f option)!

This error signifies that the version of Yosys being used cannot figure out
how to interpret the input file. For VHDL, this signifies that either GHDL
isn't being loaded properly, or that the current version of Yosys isn't compatible
with GHDL.
