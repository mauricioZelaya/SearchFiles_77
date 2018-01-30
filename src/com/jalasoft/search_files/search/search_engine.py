"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import os

from src.com.jalasoft.search_files.search import asset
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER


class Search(object):
    """

    :param object  class
    """
    def __init__(self, file_name=None, path_file='/', criteria=3):
        """
        constructor method
        :param file_name:
        :param path_file:
        :param criteria: 1 files only, 2 folders only, 3 all
        """
        self._path_file = path_file
        self._file_name = file_name
        self._criteria = criteria
        self._total_of_matches = 0

    def set_path(self, path_directory):
        """
        seth a new path for a new search
        :param path_directory:
        :return:
        """
        self._path_file = path_directory

    def get_path(self):
        """

        :return:
        """
        return self._path_file

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

    def get_criteria(self):
        """

        :return:
        """
        return self._criteria

    def set_criteria(self, criteria):
        """

        :param criteria:
        :return:
        """
        LOGGER.info("=========start setting new value for search criteria=========")

        self._criteria = criteria

        LOGGER.info("=========end setting new value for search criteria=========")
        LOGGER.debug("=========end setting new value for search criteria=========" + str(self._criteria))

    def get_total_matches(self):
        """

        :return:
        """
        return self._total_of_matches

    def print_directory(self):
        """

        :return: list of files and folders on the given path in which the search object was created
        """
        list_dir = []
        for root, dirs, files in os.walk(self._path_file, topdown=False):
            if self._criteria == 2 or self._criteria == 3:
                for value in dirs:
                    directory = asset.Folder()
                    directory.set_file_name(os.path.join(root, value))
                    directory.set_is_directory(True)
                    list_dir.append(directory)
            if self._criteria == 1 or self._criteria == 3:
                for value in files:
                    file_name = os.path.join(root, value)
                    file = asset.File()
                    file.set_file_name(file_name)
                    file.set_is_directory(False)
                    file.set_file_size(os.path.getsize(file_name))
                    list_dir.append(file)
        return list_dir

    def create_list_of_ocurrences(self):
        """

        :return:
        """
        list_of_found = []
        list_from_path = self.print_directory()
        for result in list_from_path:
            if self._file_name in os.path.basename(result.get_file_name()):
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found
