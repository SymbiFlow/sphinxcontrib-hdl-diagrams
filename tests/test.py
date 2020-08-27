#!/usr/bin/env python3

import os
import shutil
import unittest

from jinja2 import Environment, FileSystemLoader
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace

VERILOG_DIAGRAMS_PATH = os.path.abspath("..")


def get_sphinx_dirs(test_build_dir):
    sphinx_dirs = {
        "srcdir": test_build_dir,
        "confdir": test_build_dir,
        "outdir": os.path.join(test_build_dir, "build"),
        "doctreedir": os.path.join(test_build_dir, "build", "doctrees")
    }
    return sphinx_dirs


def generate_sphinx_config(test_build_dir, **jinja_dict):
    sphinx_config_path = os.path.join(test_build_dir, "conf.py")

    with open(sphinx_config_path, "w") as fd:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("conf.py.template")
        template.stream(**jinja_dict).dump(fd)


class TestSkins(unittest.TestCase):

    TEST_CASE_NAME = "TestSkins"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_netlistsvg_diagram(self):
        TEST_NAME = "test_skins"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_skins/test_skins.rst",
            "test_skins/skin-orange.svg",
            "test_skins/skin-yellow.svg",
            "verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "verilog_diagrams_path": "'{}'".format(VERILOG_DIAGRAMS_PATH),
            "master_doc": "'test_skins'",
            "custom_variables": "verilog_diagram_skin = os.path.realpath('skin-orange.svg')"
        }

        # Create the TestCase build directory
        os.makedirs(TEST_BUILD_DIR, exist_ok=True)

        # Generate a Sphinx config
        generate_sphinx_config(TEST_BUILD_DIR, **TEST_JINJA_DICT)

        # Copy the test files
        for src in TEST_FILES:
            src_basename = os.path.basename(src)
            dst = os.path.join(TEST_BUILD_DIR, src_basename)
            shutil.copyfile(src, dst)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)


class TestYosysScript(unittest.TestCase):

    TEST_CASE_NAME = "TestYosysScript"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_yosys_script(self):
        TEST_NAME = "test_yosys_script"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_yosys_script/test_yosys_script.rst",
            "test_yosys_script/yosys_script.ys",
            "test_yosys_script/yosys_script2.ys",
            "verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "verilog_diagrams_path": "'{}'".format(VERILOG_DIAGRAMS_PATH),
            "master_doc": "'test_yosys_script'",
            "custom_variables": "verilog_diagram_yosys_script = os.path.realpath('yosys_script.ys')"
        }

        # Create the TestCase build directory
        os.makedirs(TEST_BUILD_DIR, exist_ok=True)

        # Generate a Sphinx config
        generate_sphinx_config(TEST_BUILD_DIR, **TEST_JINJA_DICT)

        # Copy the test files
        for src in TEST_FILES:
            src_basename = os.path.basename(src)
            dst = os.path.join(TEST_BUILD_DIR, src_basename)
            shutil.copyfile(src, dst)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)


if __name__ == '__main__':
    unittest.main()
