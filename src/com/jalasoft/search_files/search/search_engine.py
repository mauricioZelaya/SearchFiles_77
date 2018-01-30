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
    def __init__(self, search_criteria):
        """
        constructor method
        :type search_criteria: object type SearchCritera
        
        """
        self._search_criteria = search_criteria
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
        search_criteria_values = self._search_criteria.get_basic_search()
        for root, dirs, files in os.walk(search_criteria_values['path'], topdown=False):
            if search_criteria_values['criteria'] == 2 or search_criteria_values['criteria'] == 3:
                for value in dirs:
                    directory = asset.Folder()
                    directory.set_file_name(os.path.join(root, value))
                    directory.set_is_directory(True)
                    list_dir.append(directory)
            if search_criteria_values['criteria'] == 1 or search_criteria_values['criteria'] == 3:
                for value in files:
                    file_name = os.path.join(root, value)
                    file = asset.File()
                    file.set_file_name(file_name)
                    file.set_is_directory(False)
                    file.set_file_size(os.path.getsize(file_name))
                    list_dir.append(file)
        return list_dir

    def create_list_of_ocurrences(self, search_criteria):
        """

        :return:
        """
        list_of_found = []
        list_from_path = self.print_directory()
        file_name = search_criteria.get_basic_search()
        for result in list_from_path:
            if file_name['file_name'] in os.path.basename(result.get_file_name()):
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found


# search = Search(path_file='D:\MauricioZ\Documments\Personal\\videos', criteria=2, file_name='Franco')
# listM = search.create_list_of_ocurrences()
# for value in listM:
#     print(value.get_file_name())
    # print("File Size: %s Mbytes" % str(int(value.get_file_size())/1000000))
    # print("creation date: %s" % value.get_creation_time())
# print('hi')
# print(os.path.basename('D:\MauricioZ\Documments\Courses\Dev Fundamentals\module_2\SearchFiles_77\\test\mauricio.txt'))
