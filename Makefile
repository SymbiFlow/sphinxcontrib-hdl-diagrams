# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

# The top directory where environment will be created.
TOP_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

# A pip `requirements.txt` file.
# https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format
REQUIREMENTS_FILE := requirements.txt

# A conda `environment.yml` file.
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
ENVIRONMENT_FILE := environment.yml

# Rule to checkout the git submodule if it wasn't cloned.
$(TOP_DIR)/third_party/make-env/conda.mk: $(TOP_DIR)/.gitmodules
	cd $(TOP_DIR); git submodule update --init third_party/make-env
	touch $(TOP_DIR)/third_party/make-env/conda.mk

-include $(TOP_DIR)/third_party/make-env/conda.mk

# Create a version.py file
VERSION_PY = sphinxcontrib_hdl_diagrams/version.py
$(VERSION_PY):
	@echo "__version__ = '$$(git describe | sed -e's/v\([0-9]\+\)\.\([0-9]\+\)-\([0-9]\+\)-g[0-9a-f]\+/\1.\2.post\3/')'" > $@

.PHONY: $(VERSION_PY)

version:
	@if $$(git rev-parse --is-shallow-repository); then git fetch --unshallow; fi
	git fetch origin --tags
	@$(MAKE) $(VERSION_PY)
	@cat $(VERSION_PY)

version-clean:
	rm -f $(VERSION_PY)

.PHONY: version-clean

clean:: version-clean

# Build the package locally
# -------------------------------------

build: $(VERSION_PY) | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) python setup.py sdist bdist_wheel && twine check dist/*

build-clean:
	rm -rf env/downloads/conda-pkgs
	rm -rf build dist *.egg-info
	find -name *.pyc -delete
	find -name __pycache__ -delete

.PHONY: build build-clean

clean:: build-clean

# Upload the package to PyPi
# -------------------------------------

#PYPI_TEST = --repository-url https://test.pypi.org/legacy/
#PYPI_TEST = --repository testpypi

upload-test: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload ${PYPI_TEST}  dist/*

.PHONY: upload-test

upload: build | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) twine upload --verbose dist/*

.PHONY: upload

# Tests
# -------------------------------------

test: $(VERSION_PY) | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd docs; make html
	$(IN_CONDA_ENV) cd tests; make test

.PHONY: test

# Build and upload compatibility package
# -------------------------------------

COMPAT_PACKAGE_DIR = compat

build_compat: $(VERSION_PY) | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd $(COMPAT_PACKAGE_DIR); python setup.py sdist bdist_wheel && twine check dist/*

build_compat-clean:
	cd $(COMPAT_PACKAGE_DIR); rm -rf env/downloads/conda-pkgs
	cd $(COMPAT_PACKAGE_DIR); rm -rf build dist *.egg-info
	cd $(COMPAT_PACKAGE_DIR); find -name *.pyc -delete
	cd $(COMPAT_PACKAGE_DIR); find -name __pycache__ -delete

.PHONY: build_compat build_compat-clean

clean:: build_compat-clean

upload_compat-test: build_compat | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd $(COMPAT_PACKAGE_DIR); twine upload ${PYPI_TEST}  dist/*

upload_compat: build_compat | $(CONDA_ENV_PYTHON)
	$(IN_CONDA_ENV) cd $(COMPAT_PACKAGE_DIR); twine upload --verbose dist/*

.PHONY: upload_compat-test upload_compat
