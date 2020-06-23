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

# Build and upload commands
build: | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) python setup.py sdist bdist_wheel

.PHONY: build

#PYPI_TEST = --repository-url https://test.pypi.org/legacy/
#PYPI_TEST = --repository testpypi

upload-test: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload ${PYPI_TEST}  dist/*

.PHONY: upload-test

upload: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload --verbose dist/*

.PHONY: upload

test: | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd docs; make html
