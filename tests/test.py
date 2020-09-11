#!/usr/bin/env python3

import os
import shutil
import unittest

from jinja2 import Environment, FileSystemLoader
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace

HDL_DIAGRAMS_PATH = os.path.abspath("..")

## Helpers

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

## Base class for tests

class TestBase(unittest.TestCase):

    def print_test_header(self, case_name, test_name):
        print("")
        print("# ---------------------------------------------------------- #")
        print("# TEST CASE: {}".format(case_name))
        print("# TEST NAME: {}".format(test_name))
        print("# ---------------------------------------------------------- #")
        print("")

    def prepare_test(self, test_name, test_build_dir, test_files, **test_jinja_dict):
        self.print_test_header(self.TEST_CASE_NAME, test_name)

        # Create the TestCase build directory
        os.makedirs(test_build_dir, exist_ok=True)

        # Generate a Sphinx config
        generate_sphinx_config(test_build_dir, **test_jinja_dict)

        # Copy the test files
        for src in test_files:
            src_basename = os.path.basename(src)
            dst = os.path.join(test_build_dir, src_basename)
            shutil.copyfile(src, dst)


## Test cases

class TestSkins(TestBase):

    TEST_CASE_NAME = "TestSkins"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_netlistsvg_diagram(self):
        TEST_NAME = "test_skins"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_skins/test_skins.rst",
            "test_skins/skin-purple.svg",
            "test_skins/skin-yellow.svg",
            "code/verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_skins'",
            "custom_variables": "hdl_diagram_skin = os.path.realpath('skin-purple.svg')"
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)


class TestYosysScript(TestBase):

    TEST_CASE_NAME = "TestYosysScript"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_yosys_script(self):
        TEST_NAME = "test_yosys_script"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_yosys_script/test_yosys_script.rst",
            "test_yosys_script/yosys_script.ys",
            "test_yosys_script/yosys_script2.ys",
            "code/verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_yosys_script'",
            "custom_variables": "hdl_diagram_yosys_script = os.path.realpath('yosys_script.ys')"
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

class TestYosysType(TestBase):

    TEST_CASE_NAME = "TestYowasp"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_yosys_yowasp(self):
        TEST_NAME = "test_yosys_yowasp"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_yosys_type/test_yosys_yowasp.rst",
            "code/verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_yosys_yowasp'",
            "custom_variables": ""
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

    @unittest.skipIf(shutil.which('yosys') is None, 'Skipping test_yosys_system. Yosys is not installed!')
    def test_yosys_system(self):
        TEST_NAME = "test_yosys_system"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_yosys_type/test_yosys_system.rst",
            "code/verilog/adder.v"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_yosys_system'",
            "custom_variables": "hdl_diagram_yosys = 'system'"
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

    @unittest.skipIf(shutil.which('yosys') is None, 'Skipping test_yosys_path. Yosys is not installed!')
    def test_yosys_path(self):
        TEST_NAME = "test_yosys_path"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_yosys_type/test_yosys_path.rst",
            "code/verilog/adder.v"
        ]

        yosys_path = shutil.which("yosys")

        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_yosys_path'",
            "custom_variables": "hdl_diagram_yosys = '{}'".format(yosys_path)
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

class TestNMigen(TestBase):

    TEST_CASE_NAME = "TestNMigen"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_yosys_script(self):
        TEST_NAME = "test_nmigen"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_nmigen/test_nmigen.rst",
            "code/nmigen/counter.py"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_nmigen'",
            "custom_variables": "''"
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

class TestRTLIL(TestBase):

    TEST_CASE_NAME = "TestRTLIL"
    TEST_CASE_BUILD_DIR = os.path.join("build", TEST_CASE_NAME)

    def test_yosys_script(self):
        TEST_NAME = "test_rtlil"
        TEST_BUILD_DIR = os.path.join("build", self.TEST_CASE_NAME, TEST_NAME)
        TEST_FILES = [
            "test_rtlil/test_rtlil.rst",
            "code/rtlil/counter.il"
        ]
        TEST_JINJA_DICT = {
            "hdl_diagrams_path": "'{}'".format(HDL_DIAGRAMS_PATH),
            "master_doc": "'test_rtlil'",
            "custom_variables": "''"
        }

        self.prepare_test(TEST_NAME, TEST_BUILD_DIR, TEST_FILES, **TEST_JINJA_DICT)

        # Run the Sphinx
        sphinx_dirs = get_sphinx_dirs(TEST_BUILD_DIR)
        with docutils_namespace():
            app = Sphinx(buildername="html", warningiserror=True, **sphinx_dirs)
            app.build(force_all=True)

if __name__ == '__main__':
    unittest.main()
