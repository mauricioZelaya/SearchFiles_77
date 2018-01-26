"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import os

from src.com.jalasoft.search_files.search import asset


class Search(object):
    """

    :param object  class
    """
    def __init__(self, file_name=None, path_file='/', criteria=None):
        """
        constructor method
        :param file_name:
        :param path_file:
        :param criteria:
        """
        self._path_file = path_file
        self._file_name = file_name
        self._criteria = criteria

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

    def print_directory(self):
        """

        :return: list of files and folders on the given path in which the search object was created
        """
        list_dir = []
        for root, dirs, files in os.walk(self._path_file, topdown=False):
            for value in dirs:
                directory = asset.Folder()
                directory.set_file_name(os.path.join(root, value)+'\\')
                directory.set_is_directory(True)
                list_dir.append(directory)
            for value in files:
                file_name = os.path.join(root, value)
                file = asset.File()
                file.set_file_name(file_name)
                file.set_is_directory(False)
                file.set_file_size(os.path.getsize(file_name))
                list_dir.append(file)
        return list_dir

    def create_list_of_ocurrences(self):
        list_of_found = []
        list_from_path = self.print_directory()
        for result in list_from_path:
            if self._file_name in result:
                list_of_found.append(result)
        return list_of_found


search = Search(path_file='D:\MauricioZ\Documments\Courses\Dev Fundamentals\module_2\SearchFiles_77\config\\')
listM = search.print_directory()
for value in listM:
    print(value.get_file_name())
