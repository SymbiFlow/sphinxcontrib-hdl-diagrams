no-license
==========

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

Example
+++++++

Verilog Code Block (with license header)
----------------------------------------

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. literalinclude:: ../code/verilog/dff.v
      :language: verilog
      :linenos:

Result
******

.. literalinclude:: ../code/verilog/dff.v
   :language: verilog
   :linenos:


Verilog Code Block (without license header)
-------------------------------------------

RST Directive
*************

.. code-block:: rst
   :linenos:

   .. no-license:: ../code/verilog/dff.v
      :language: verilog
      :linenos:

Result
******

.. no-license:: ../code/verilog/dff.v
   :language: verilog
   :linenos:
