# Copyright (C) 2020  SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

# The top directory where environment will be created.
TOP_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

# A pip `requirements.txt` file.
# https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format
REQUIREMENTS_FILE := requirements.txt

# A conda `environment.yml` file.
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
ENVIRONMENT_FILE := environment.yml

include third_party/make-env/conda.mk

# Create a version.py file
VERSION_PY = sphinxcontrib_verilog_diagrams/version.py
$(VERSION_PY):
	echo "__version__ = '$$(git describe | sed -e's/v\([0-9]\+\)\.\([0-9]\+\)-\([0-9]\+\)-g[0-9a-f]\+/\1.\2.post\3/')'" > $@

.PHONY: $(VERSION_PY)

version-clean:
	rm -f $(VERSION_PY)

.PHONY: version-clean

clean: version-clean

# Build and upload commands
build: $(VERSION_PY) | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) python setup.py sdist bdist_wheel && twine check dist/*

.PHONY: build

build-clean:
	rm -rf env/downloads/conda-pkgs
	rm -rf build dist *.egg-info
	find -name *.pyc -delete
	find -name __pycache__ -delete

clean: build-clean

#PYPI_TEST = --repository-url https://test.pypi.org/legacy/
#PYPI_TEST = --repository testpypi

upload-test: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload ${PYPI_TEST}  dist/*

.PHONY: upload-test

upload: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload --verbose dist/*

.PHONY: upload

test: $(VERSION_PY) | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd docs; make html

.PHONY: test
