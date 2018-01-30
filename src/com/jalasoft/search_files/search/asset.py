"""
asset class and inheritances
"""

import os


class Asset(object):
    """

    """
    def __init__(self):
        self._file_name = ''
        self.file_size = 0
        self.is_directory = False

    def get_file_name(self):
        """

        :return:
        """
        return self._file_name

    def get_file_size(self):
        """

        :return:
        """
        return self.file_size

    def get_is_directory(self):
        """

        :return:
        """
        return self.is_directory

    def get_creation_time(self):
        """
        return metadata information about the creation date of the asset
        :return:
        """
        return os.path.getctime(self._file_name)


class File(Asset):
    """

    """
    def set_file_name(self, file_name):
        """

        :param file_name:
        :return:
        """
        self._file_name = file_name

    def set_file_size(self, file_size):
        """

        :param file_size:
        :return:
        """
        self.file_size = file_size

    def set_is_directory(self, is_directory):
        """

        :param is_directory:
        :return:
        """
        self.is_directory = is_directory


class Folder(Asset):
    """

    """

    def set_file_name(self, file_name):
        """

        :param file_name:
        :return:
        """
        self._file_name = file_name

    def set_is_directory(self, is_directory):
        """

        :param is_directory:
        :return:
        """
        self.is_directory = is_directory
