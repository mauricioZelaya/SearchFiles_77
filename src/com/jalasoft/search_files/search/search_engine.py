"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import os


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
                list_dir.append(os.path.join(root, value))
            for value in files:
                list_dir.append(os.path.join(root, value))

        return list_dir

    def create_list_of_ocurrences(self):
        list_of_found = []
        list_from_path = self.print_directory()
        for result in list_from_path:
            if self._file_name in result:
                list_of_found.append(result)
        return list_of_found


search = Search(path_file='D:\\',
                file_name='video')
dict = search.create_list_of_ocurrences()
print(dict)

        # for root, dirs, files in os.walk(self._path_file, topdown=False):
        #
        #     for value in dirs:
        #         file = File()
        #         file.set_path(os.path.join(root, value))
        #         file.set_is_file(False)
        #         file.se_size(os.path.getSize(os.path.join(root, value)))
        #         list_dir.append(file)
        #
        #     for value in files:
        #         list_dir.append(os.path.join(root, value))
        #
        # return list_dir
