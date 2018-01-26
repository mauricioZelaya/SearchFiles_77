"""
This module contain the unitests for the utils module
"""

import os
import pytest
import config.config as config
import src.com.jalasoft.search_files.utils.utils as utils

@pytest.mark.utils
def test_is_a_valid_path_with_valid_path():
    """
    This method will validate that the path is correct for the OS
    :return: None
    """
    path = os.getcwd()
    assert utils.is_a_valid_path(path)["valid"]

@pytest.mark.utils
def test_is_a_valid_path_with_invalid_path():
    """
    This method will validate that the path is invalid for the OS
    :return: None
    """
    path = "D:\\"
    assert not utils.is_a_valid_path(path)["valid"]

@pytest.mark.utils
def test_is_a_valid_path_with_valid_wildcards():
    """
    This method will verify that path has only valid wildcards
    :return: None
    """
    if config.__OS_PLATFORM__ == "win32":
        path = os.getcwd()
        assert utils.is_a_valid_path(path)["valid"]
    else:
        path = os.getcwd()
        assert utils.is_a_valid_path(path)["valid"]

@pytest.mark.utils
def test_is_a_valid_path_with_invalid_wildcards():
    """
    This method will verify that path is rejected when it has invalid wildcards
    :return: None
    """
    if config.__OS_PLATFORM__ == "win32":
        path = os.getcwd() + "\\wong>path"
        assert utils.is_a_valid_path(path)["valid"]

@pytest.mark.utils
def test_validate_correct_path_for_linux():
    """
    This test will validate if the path is correct for a linux OS
    :return: None
    """
    path = "/"
    assert utils._validate_path_match_os(path)

@pytest.mark.utils
def test_validate_incorrect_path_for_linux():
    """
    This test will validate an incorrect path for a linux OS
    :return: None
    """
    path = "D:\\"
    assert not utils._validate_path_match_os(path)

@pytest.mark.utils
def test_validate_valid_wildcards_in_path():
    """
    This test will validate that the path has no forbidden wildcards
    :return: None
    """
    path = "C:\\Users\\Some random dir"
    assert utils._is_path_with_valid_values(path)

@pytest.mark.utils
def test_validate_invalid_wildcards_in_path():
    """
    This test will validate that the path has forbidden wildcards
    if the test fail in a linux machine is expected
    :return: None
    """
    path = "C:\\Use>rs\\Some random dir"
    if config.__OS_PLATFORM__ == "win32":
        assert not utils._is_path_with_valid_values(path)
    else:
        assert utils._is_path_with_valid_values(path)

@pytest.mark.utils
def test_is_object_a_directory():
    """
    This test will verify that the object is a directory
    :return: None
    """
    path = os.getcwd()
    assert utils.is_object_directory(path)

@pytest.mark.utils
def test_is_object_not_a_directory():
    """
    This test will verify that the object is not a directory
    :return: None
    """
    path = os.getcwd()
    path = path + "/something,txt"
    assert not utils.is_object_directory(path)
