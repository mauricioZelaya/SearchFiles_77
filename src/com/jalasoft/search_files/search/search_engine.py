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
        self._list_of_found = []

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
        search_criteria_values = self._search_criteria.get_search_filter()
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
        list_from_path = self.print_directory()
        file_name = search_criteria.get_search_filter()
        for result in list_from_path:
            if file_name['file_name'] in os.path.basename(result.get_file_name()):
                self._list_of_found.append(result)
                self._total_of_matches += 1
        return self._list_of_found

    def filtering_results(self, search_criteria):
        list_from_path = self.print_directory()

# search = Search(path_file='D:\MauricioZ\Documments\Personal\\videos', criteria=2, file_name='Franco')
# listM = search.create_list_of_ocurrences()
# for value in listM:
#     print(value.get_file_name())
#     print("File Size: %s Mbytes" % str(int(value.get_file_size())/1000000))
#     print("creation date: %s" % value.get_creation_time())
# print('hi')
# print(os.path.basename('D:\MauricioZ\Documments\Courses\Dev Fundamentals\module_2\SearchFiles_77\\test\mauricio.txt'))
