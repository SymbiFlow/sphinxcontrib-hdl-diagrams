sphinxcontrib-verilog-diagrams
==============================

[![PyPI](https://img.shields.io/pypi/v/sphinxcontrib-verilog-diagrams.svg)](https://pypi.python.org/pypi/sphinxcontrib-verilog-diagrams)
[![PyPI version](https://img.shields.io/pypi/pyversions/sphinxcontrib-verilog-diagrams.svg)](https://pypi.python.org/pypi/sphinxcontrib-verilog-diagrams)
[![Documentation](https://readthedocs.org/projects/sphinxcontrib-verilog-diagrams/badge)](https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.com/SymbiFlow/sphinxcontrib-verilog-diagrams.svg?branch=master)](https://travis-ci.com/SymbiFlow/sphinxcontrib-verilog-diagrams)
[![codecov](https://codecov.io/gh/SymbiFlow/sphinxcontrib-verilog-diagrams/branch/master/graph/badge.svg)](https://codecov.io/gh/SymbiFlow/sphinxcontrib-verilog-diagrams)

--------------------------------------------------------------------------------

Sphinx Extension which generates various types of diagrams from Verilog code.

[sphinxcontrib-verilog-diagrams](https://github.com/SymbiFlow/sphinxcontrib-verilog-diagrams)
is a Sphinx extension to make it easier to write nice documentation from
Verilog files. It primarily uses [Yosys](https://github.com/YosysHQ/yosys) to do the Verilog reading.

Check out the [documentation](https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest) for examples.

## Installation

Python 3.5+ is required.

```
pip install sphinxcontrib-verilog-diagrams
```

Or,

```
python3 -m pip install sphinxcontrib-verilog-diagrams
```

### Sphinx Integration

In your conf.py, add the following lines.

```python
extensions = [
    ...,
    'sphinxcontrib_verilog_diagrams',
]
```

## Non-Python Dependencies

These dependencies can be either installed on your system or install using the
conda `environment.yml` file with;

```bash
conda XXXX
```


### Required

 * [`yosys`](https://github.com/YosysHQ/yosys)

### Optional

 * [`netlistsvg`](https://github.com/nturley/netlistsvg)

## Usage

The `verilog-diagram` RST directive can be used to generate a diagram from Verilog code and include it in your documentation.
Check out the [examples](https://sphinxcontrib-verilog-diagrams.readthedocs.io/en/latest/) to see how to use it.

```rst

.. verilog-diagram:: file.v
   :type: XXXXX
   :module: XXXX
   :flatten:

```

### Options

`:type:` - Verilog Diagram Types;

 * `yosys-blackbox` - Netlist rendered by Yosys.
 * `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
 * `netlistsvg` - Render output with [netlistsvg](https://github.com/nturley/netlistsvg)

`:module:` - Which module to diagram.

`:flatten:` - Use the Yosys `flatten` command before generating the image.

### Example

Here is a diagram of a 4-bit carry chain.

![4-bit carry chain](./carry4-flatten.svg)


## Licence

[Apache 2.0](LICENSE)
