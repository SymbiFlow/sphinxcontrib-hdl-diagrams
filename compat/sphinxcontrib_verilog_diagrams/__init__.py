import warnings
import sphinxcontrib_hdl_diagrams

def setup(app):
    deprecation_msg = """
    sphinxcontrib-verilog-diagram extension is depreciated!
    Please use sphinxcontrib-hdl-diagrams instead:
    https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams"""
    warnings.warn(deprecation_msg, DeprecationWarning)

    return sphinxcontrib_hdl_diagrams.setup(app)
