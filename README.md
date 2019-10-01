sphinxcontrib-verilog-diagrams
==============================

[![PyPI](https://img.shields.io/pypi/v/sphinx-verilog-diagrams.svg)](https://pypi.python.org/pypi/sphinx-verilog-diagrams)
[![PyPI version](https://img.shields.io/pypi/pyversions/sphinx-verilog-diagrams.svg)](https://pypi.python.org/pypi/sphinx-verilog-diagrams)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://mithro.github.io/sphinx-verilog-diagrams)
[![Build Status](https://travis-ci.org/mithro/sphinx-verilog-diagrams.svg?branch=master)](https://travis-ci.org/mithro/sphinx-verilog-diagrams)
[![codecov](https://codecov.io/gh/mithro/sphinx-verilog-diagrams/branch/master/graph/badge.svg)](https://codecov.io/gh/mithro/sphinx-verilog-diagrams)

--------------------------------------------------------------------------------

Sphinx Extension which generates various types of diagrams from Verilog code.

sphinx-verilog-diagrams is an extension to Sphinx to make it easier to write nice
documentation from Verilog files.

It primarily uses Yosys to do the Verilog reading.

## Installation

Python 3.5+ is required.

```
pip install sphinx-verilog-diagrams
```

Or,

```
python3 -m pip install sphinx-verilog-diagrams
```

### Sphinx Integration

In your conf.py, add the following lines.

```python
extensions = [
    ...,
    'sphinx_verilog_diagrams',
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

 * `netlistsvg`

## New Directives

```rst

.. verilog-diagram:: file.v
   :type: XXXXX
   :module: XXXX
   :flatten:

```

Verilog Diagram Types;

 * `yosys-blackbox` - Netlist rendered by Yosys.
 * `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
 * `netlistsvg` - Render output with [netlistsvg]()

`:module:` - Which module to diagram.

`:flatten:` - Use the Yosys `flatten` command before generating the image.

`

## Licence

[Apache 2.0](LICENSE)
