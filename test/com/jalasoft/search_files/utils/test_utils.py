"""
This module contain the unitests for the utils module
"""

import os
import pytest
import config.config as config
import src.com.jalasoft.search_files.utils.utils as utils
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

@pytest.mark.utils
def test_is_a_valid_path_with_valid_path():
    """
    This method will validate that the path is correct for the OS
    :return: None
    """
    LOGGER.info("=========test_is_a_valid_path_with_valid_path is starting=========")

    path = os.getcwd()
    assert utils.is_a_valid_path(path)["valid"]

    LOGGER.info("=========test_is_a_valid_path_with_valid_path has PASSED=========")

@pytest.mark.utils
def test_is_a_valid_path_with_invalid_path():
    """
    This method will validate that the path is invalid for the OS
    :return: None
    """
    LOGGER.info("=========test_is_a_valid_path_with_invalid_path is starting=========")

    path = "D:\\"
    assert not utils.is_a_valid_path(path)["valid"]

    LOGGER.info("=========test_is_a_valid_path_with_invalid_path has PASSED=========")


@pytest.mark.utils
def test_is_a_valid_path_with_valid_wildcards():
    """
    This method will verify that path has only valid wildcards
    :return: None
    """
    LOGGER.info("=========test_is_a_valid_path_with_valid_wildcards is starting=========")

    if config.__OS_PLATFORM__ == "win32":
        path = os.getcwd()
        assert utils.is_a_valid_path(path)["valid"]
    else:
        path = os.getcwd()
        assert utils.is_a_valid_path(path)["valid"]

    LOGGER.info("=========test_is_a_valid_path_with_valid_wildcards has PASSED=========")


@pytest.mark.utils
def test_is_a_valid_path_with_invalid_wildcards():
    """
    This method will verify that path is rejected when it has invalid wildcards
    :return: None
    """
    LOGGER.info("=========test_is_a_valid_path_with_invalid_wildcards is starting=========")

    if config.__OS_PLATFORM__ == "win32":
        path = os.getcwd() + "\\wong>path"
        assert utils.is_a_valid_path(path)["valid"]

    LOGGER.info("=========test_is_a_valid_path_with_invalid_wildcards has PASSED=========")


@pytest.mark.utils
def test_validate_correct_path_for_linux():
    """
    This test will validate if the path is correct for a linux OS
    :return: None
    """
    LOGGER.info("=========test_validate_correct_path_for_linux is starting=========")

    path = "/"
    assert utils._validate_path_match_os(path)

    LOGGER.info("=========test_validate_correct_path_for_linux has PASSED=========")


@pytest.mark.utils
def test_validate_incorrect_path_for_linux():
    """
    This test will validate an incorrect path for a linux OS
    :return: None
    """
    LOGGER.info("=========test_validate_incorrect_path_for_linux is starting=========")

    path = "D:\\"
    assert not utils._validate_path_match_os(path)

    LOGGER.info("=========test_validate_incorrect_path_for_linux has PASSED=========")


@pytest.mark.utils
def test_validate_valid_wildcards_in_path():
    """
    This test will validate that the path has no forbidden wildcards
    :return: None
    """
    LOGGER.info("=========test_validate_valid_wildcards_in_path is starting=========")

    path = "C:\\Users\\Some random dir"
    assert utils._is_path_with_valid_values(path)

    LOGGER.info("=========test_validate_valid_wildcards_in_path has PASSED=========")


@pytest.mark.utils
def test_validate_invalid_wildcards_in_path():
    """
    This test will validate that the path has forbidden wildcards
    if the test fail in a linux machine is expected
    :return: None
    """
    LOGGER.info("=========test_validate_invalid_wildcards_in_path is starting=========")

    path = "C:\\Use>rs\\Some random dir"
    if config.__OS_PLATFORM__ == "win32":
        assert not utils._is_path_with_valid_values(path)
    else:
        assert utils._is_path_with_valid_values(path)

    LOGGER.info("=========test_validate_invalid_wildcards_in_path has PASSED=========")


@pytest.mark.utils
def test_is_object_a_directory():
    """
    This test will verify that the object is a directory
    :return: None
    """
    LOGGER.info("=========test_is_object_a_directory is starting=========")

    path = os.getcwd()
    assert utils.is_object_directory(path)

    LOGGER.info("=========test_is_object_a_directory has PASSED=========")


@pytest.mark.utils
def test_is_object_not_a_directory():
    """
    This test will verify that the object is not a directory
    :return: None
    """
    LOGGER.info("=========test_is_object_not_a_directory is starting=========")

    path = os.getcwd()
    path = path + "/something,txt"
    assert not utils.is_object_directory(path)

    LOGGER.info("=========test_is_object_not_a_directory has PASSED=========")

