import sphinxcontrib_hdl_diagrams

def setup(app):
    print("")
    print("WARNING:")
    print("  sphinxcontrib-verilog-diagram extension is depreciated!")
    print("  Please use sphinxcontrib-hdl-diagrams instead:")
    print("  https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams")
    print("")

    return sphinxcontrib_hdl_diagrams.setup(app)
