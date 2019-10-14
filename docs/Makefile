# Minimal makefile for Sphinx documentation
#

MAKEDIR := $(dir $(lastword $(MAKEFILE_LIST)))

# You can set these variables from the command line.
SPHINXOPTS      =
SPHINXBUILD     = [ -e conda/bin/activate ] && source conda/bin/activate; sphinx-build
SPHINXAUTOBUILD = [ -e conda/bin/activate ] && source conda/bin/activate; sphinx-autobuild
SPHINXPROJ      = SphinxVerilog
SOURCEDIR       = .
BUILDDIR        = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	@$(SPHINXAUTOBUILD) -b html --ignore \*.swp --ignore \*~ $(SPHINXOPTS) "$(SOURCEDIR)" "$(BUILDDIR)/html"

.PHONY: help livehtml Makefile


conda/Miniconda3-latest-Linux-x86_64.sh:
	mkdir conda
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda/Miniconda3-latest-Linux-x86_64.sh
	chmod a+x conda/Miniconda3-latest-Linux-x86_64.sh

conda:
	rm -rf conda
	make conda/Miniconda3-latest-Linux-x86_64.sh
	./conda/Miniconda3-latest-Linux-x86_64.sh -p $(PWD)/conda -b -f
	source conda/bin/activate; conda config --system --add envs_dirs $(PWD)/conda/envs
	source conda/bin/activate; conda config --system --add pkgs_dirs $(PWD)/conda/pkgs
	source conda/bin/activate; conda env update --name base --file ../environment.yml

.PHONY: conda

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
