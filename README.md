sphinx-verilog
==============

[![PyPI](https://img.shields.io/pypi/v/sphinx-verilog.svg)](https://pypi.python.org/pypi/sphinx-verilog)
[![PyPI version](https://img.shields.io/pypi/pyversions/sphinx-verilog.svg)](https://pypi.python.org/pypi/sphinx-verilog)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://mithro.github.io/sphinx-verilog)
[![Build Status](https://travis-ci.org/mithro/sphinx-verilog.svg?branch=master)](https://travis-ci.org/mithro/sphinx-verilog)
[![codecov](https://codecov.io/gh/mithro/sphinx-verilog/branch/master/graph/badge.svg)](https://codecov.io/gh/mithro/sphinx-verilog)

--------------------------------------------------------------------------------

sphinx-verilog is an extension to Sphinx to make it easier to write nice
documentation from Verilog files.

It primarily uses Yosys to do the Verilog reading.

## Installation

Python 3.5+ is required.

```
pip install sphinx-verilog
```

Or,

```
python3 -m pip install sphinx-verilog
```

### Sphinx Integration

In your conf.py, add the following lines.

```python
extensions = [
    ...,
    'sphinx_verilog',
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
   :type:
   :flatten:

```

Verilog Diagram Types;

 * `yosys-blackbox` - Netlist rendered by Yosys.
 * `yosys-aig` - Verilog file run through `aigmap` before image is generated directly in Yosys.
 * `netlistsvg` - Render output with [netlistsvg]()

`:flatten:` - Use the Yosys `flatten` command before generating the image.


## Licence

[Apache 2.0](https://github.com/mithro/sphinx-verilog/blob/master/LICENSE)
