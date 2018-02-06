"""
This package is for utilities, methods that will help to validate inputs
"""
import calendar
import os

import datetime

import config.config as config
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

def is_a_valid_path(path=None):
    """
    This method verify that the path is valid, it includes verification of the OS and the wildcards
    :param path: The path that will be tested
    :return: Boolean
    """

    if not _validate_path_match_os(path):
        LOGGER.error("method 'is_a_valid_path' fail for OS verification: ".format(path))
        return {"message": "invalid OS path",
                "valid": False}

    if not _is_path_with_valid_values(path):
        LOGGER.error("method 'is_a_valid_path' fail for wildcards verification: ".format(path))
        return {"message": "path contains invalid wildcards",
                "valid": False}

    LOGGER.info("method 'is_a_valid_path' success for verifications: ".format(path))
    return {"message": "the path is correct",
            "valid": True}


def _validate_path_match_os(path=None):
    """
    This method will validate that the path belong to the local OS
    :param path: The path that will be validate
    :return: Boolean
    """
    return os.path.isabs(path)


def _is_path_with_valid_values(path=None):
    """
    This method validates that the given path does not contain any invalid
    wildcard, it only applies for windows OS.
    :param path: The path that will be validated
    :return: Boolean
    """
    if path is None:
        return False

    if config.__OS_PLATFORM__ == "win32":
        invalid_values = ["<", ">", ":", '"', "/", "|", "?", "*"]
        path = path.split("\\")
        path.pop(0)
        for dir in path:
            for char in invalid_values:
                if char in dir:
                    return False
    return True


def is_object_directory(path):
    """
    This method will return if the path is directory
    :param path: the path that will be verified as a directory
    :return: boolean
    """
    if os.path.isdir(path):
        LOGGER.info("The object is a directory: ".format(path))
        return True
    LOGGER.error("The object is not a directory".format(path))
    return False


def convert_to_epoch_time(year, month, day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    return calendar.timegm(datetime.datetime(year, month, day, 0, 0).timetuple())


def date_to_epoch_time(date_to_convert):
    """

    :param self:
    :param date_to_convert:
    :return:
    """
    init_date = date_to_convert.split('/')
    return convert_to_epoch_time(int(init_date[0]), int(init_date[1]), int(init_date[2]))


def is_user_value_valid(user_value, option):
    pass

