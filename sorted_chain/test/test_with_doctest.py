"""This file tests the source code provided by the documentation.

See
- doctest documentation: https://docs.python.org/3/library/doctest.html
- Issue 443: https://github.com/collective/icalendar/issues/443

This file should be tests, too:

    >>> print("Hello World!")
    Hello World!

"""

import doctest
import importlib
import os
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
MODULE_PATH = HERE.parent

PYTHON_FILES = [
    Path(dirpath) / filename
    for dirpath, dirnames, filenames in os.walk(MODULE_PATH)
    for filename in filenames
    if filename.lower().endswith(".py") and "fuzzing" not in dirpath
]

MODULE_NAMES = [
    "sorted_chain" + python_file.relative_to(MODULE_PATH).with_suffix("").as_posix().replace("/", ".")
    for python_file in PYTHON_FILES
]


def test_this_module_is_among_them():
    assert __name__ in MODULE_NAMES


@pytest.mark.parametrize("module_name", MODULE_NAMES)
def test_docstring_of_python_file(module_name):
    """This test runs doctest on the Python module."""
    module = importlib.import_module(module_name)
    test_result = doctest.testmod(module, name=module_name)
    assert test_result.failed == 0, f"{test_result.failed} errors in {module_name}"


# This collection needs to exclude .tox and other subdirectories

DOCUMENTATION_PATH = Path(HERE).parent.parent.parent / "docs"

try:
    DOCUMENT_PATHS = [
        DOCUMENTATION_PATH / subdir / filename
        for subdir in ["."]
        for filename in (DOCUMENTATION_PATH / subdir).glob("*")
        if filename.lower().endswith(".md")
    ]
except FileNotFoundError as e:
    raise OSError(
        "Could not find the documentation - remove the build folder and try again."
    ) from e


@pytest.mark.parametrize(
    "filename",
    [
        "README.md",
    ],
)
def test_files_is_included(filename):
    assert any(path.endswith(filename) for path in DOCUMENT_PATHS)


@pytest.mark.parametrize("document", DOCUMENT_PATHS)
def test_documentation_file(document, tzp):
    """This test runs doctest on a documentation file.

    functions are also replaced to work.
    """
    try:
        test_result = doctest.testfile(
            document, module_relative=False, raise_on_error=True
        )
    except doctest.UnexpectedException as e:
        ty, err, tb = e.exc_info
        if issubclass(ty, ModuleNotFoundError) and err.name == "pytz":
            pytest.skip("pytz not installed, skipping this file.")
    finally:
        tzp.use_zoneinfo()
    assert (
        test_result.failed == 0
    ), f"{test_result.failed} errors in {document.name}"
