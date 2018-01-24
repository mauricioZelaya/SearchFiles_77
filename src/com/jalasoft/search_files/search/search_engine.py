"""
class Search_Engine perform the search on a given path of a given file_name applying all the desired filters
"""
import os


class Search(object):
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

    def print_directory(self):
        """

        :return: list of files and folders on the given path in which the search object was created
        """
        return os.listdir(self._path_file)




# def search_file(path, file_name):
#     for root, dirs, files in os.walk(path):
#         print(root)
#         # if file_name in files:
#         #     print("file path directory: %s" % root)
#         #     print(dirs)
#         #     print(files)
#         #     print("exist!!!")

