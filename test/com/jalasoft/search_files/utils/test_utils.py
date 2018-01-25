"""
This module contain the unitests for the utils module
"""

import pytest
import src.com.jalasoft.search_files.utils.utils as utils

@pytest.mark.utils
def test_validate_correct_path_for_linux():
    path = "/home/slevin"
    assert utils.validate_path_match_os(path)

@pytest.mark.utils
def test_validate_incorrect_path_for_linux():
    path = "D:\\home\\slevin\\"
    assert utils.validate_path_match_os(path) == False

@pytest.mark.utils
def test_validate_valid_wildcards_in_path():
    path = "C:\\Users\\Alejandro Alcocer"
    assert utils.is_path_with_valid_values(path)

@pytest.mark.utils
def test_validate_invalid_wildcards_in_path():
    path = "C:\\Use>rs\\Alejandro Alcocer"
    assert utils.is_path_with_valid_values(path) == False