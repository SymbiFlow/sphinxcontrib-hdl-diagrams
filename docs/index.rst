Sphinx HDL Diagrams
===================

sphinx-hdl-diagrams is an extension to Sphinx to make it easier to write
nice documentation from HDL source files, in the form of Verilog, nMigen,
RTLIL, or VHDL code.

You use the |hdl-diagram|_ RST directive to generate various styles of
diagrams from HDL code.

Most of the time there will be a license header at the top of source code,
which we might not want to show in the documentation.
This extension also provides the |no-license|_ RST directive which works exactly
like the `.. literalinclude` directive, but the `lines` option is overridden
to only show the lines after the license header.


.. |hdl-diagram| replace:: `.. hdl-diagram`
.. _hdl-diagram: directives/hdl-diagram.html
.. |no-license| replace:: `.. no-license`
.. _no-license: directives/no-license.html

The project repository is hosted on `GitHub <https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams>`_.

Installation
------------

Python 3.5+ is required.

.. code-block:: bash

   pip install sphinxcontrib-hdl-diagrams

Or,

.. code-block:: bash

   python3 -m pip install sphinxcontrib-hdl-diagrams

Sphinx integration
~~~~~~~~~~~~~~~~~~

In your conf.py, add the following lines.

.. code-block:: python

   extensions = [
      ...,
      'sphinxcontrib_hdl_diagrams',
   ]

Non-python dependencies
~~~~~~~~~~~~~~~~~~~~~~~
These dependencies can either be installed on your system or you can install them using the
conda `environment.yml <https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams/blob/master/environment.yml>`_ file.

- `yosys <https://github.com/YosysHQ/yosys>`_ (required)
- `netlistsvg <https://github.com/nturley/netlistsvg>`_ (optional)
- `GHDL <https://github.com/ghdl/ghdl>`_ (required for VHDL)
- `ghdl-yosys-plugin <https://github.com/ghdl/ghdl-yosys-plugin>`_ (required for VHDL)

Usage
-----

hdl-diagram
~~~~~~~~~~~

The `hdl-diagram` RST directive can be used to generate a diagram from HDL code and include it in your documentation.

.. code-block:: rst

   .. hdl-diagram:: file.v
      :type: XXXXX
      :module: XXXX
      :flatten:

Options
+++++++

`:type:` - Verilog Diagram Types;

- `yosys-blackbox` - Netlist rendered by Yosys.
- `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
- `netlistsvg` - Render output with `netlistsvg <https://github.com/nturley/netlistsvg>`_

`:module:` - Which module to diagram.

`:flatten:` - Use the Yosys `flatten` command before generating the image.

no-license
~~~~~~~~~~
The `no-license` RST directive can be used to include code without license headers.

.. code-block:: rst

   .. no-license:: file.v
      :language: verilog
      :linenos:
      :caption: examples/verilog/dff.v

Options
+++++++

This directive merely overrides the `lines` and `lineno-start` options of the `literalinclude` directive.
So, refer to `literalinclude` for the available options.

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   configuration/index
   directives/index
   examples/index
