"""
This package is for utilities, methods that will help to validate inputs
"""
import config.config as config
import os


def validate_path_match_os(path=None):
    """
    This method will validate that the path belong to the local OS
    :param path: The path that will be validate
    :return: Boolean
    """
    return os.path.isabs(path)

def is_path_with_valid_values(path=None):
    """
    This method validates that the given path does not contain any invalid
    wildcard, it only applies for windows OS.
    :param path: The path that will be validated
    :return: Boolean
    """
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
    if os.path.isdir(path): return True
    else: return False
