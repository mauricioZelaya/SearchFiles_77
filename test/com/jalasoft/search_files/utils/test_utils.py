"""
This module contain the unitests for the utils module
"""

import pytest
import src.com.jalasoft.search_files.utils.utils as utils

@pytest.mark.utils
def test_validate_correct_path_for_linux():
    """
    This test will validate if the path is correct for a linux OS
    :return: None
    """
    path = "/home/slevin"
    assert utils.validate_path_match_os(path)

@pytest.mark.utils
def test_validate_incorrect_path_for_linux():
    """
    This test will validate an incorrect path for a linux OS
    :return: None
    """
    path = "D:\\home\\slevin\\"
    assert not utils.validate_path_match_os(path)

@pytest.mark.utils
def test_validate_valid_wildcards_in_path():
    """
    This test will validate that the path has no forbidden wildcards
    :return: None
    """
    path = "C:\\Users\\Alejandro Alcocer"
    assert utils.is_path_with_valid_values(path)

@pytest.mark.utils
def test_validate_invalid_wildcards_in_path():
    """
    This test will validate that the path has forbidden wildcards
    :return: None
    """
    path = "C:\\Use>rs\\Alejandro Alcocer"
    assert not utils.is_path_with_valid_values(path)

@pytest.mark.utils
def test_is_object_a_directory():
    """
    This test will verify that the object is a directory
    :return: None
    """
    path = "/home/slevin"
    assert utils.is_object_directory(path)

@pytest.mark.utils
def test_is_object_not_a_directory():
    """
    This test will verify that the object is not a directory
    :return: None
    """
    path = "/home/slevin/something,txt"
    assert not utils.is_object_directory(path)
