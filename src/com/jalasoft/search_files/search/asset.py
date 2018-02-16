"""
asset class and inheritances
"""

import os


class Asset(object):
    """

    """
    def __init__(self):
        self._file_name = ''
        self._file_size = 0
        self._file_type = ''
        self.is_directory = False

    def set_file_name(self, file_name):
        """

        :param file_name:
        :return:
        """
        self._file_name = file_name

    def get_file_name(self):
        """

        :return:
        """
        return self._file_name

    def get_file_size(self):
        """

        :return:
        """
        return self._file_size

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

    def get_last_access_time(self):
        """
        return metadata information about the class access date of the asset
        :return:
        """
        return os.path.getatime(self._file_name)

    def get_last_modification_date(self):
        """
        return metadata information about the last modification date of the asset
        :return:
        """
        return os.path.getmtime(self._file_name)

    def get_file_type(self):
        """

        :return:
        """
        return self._file_type

