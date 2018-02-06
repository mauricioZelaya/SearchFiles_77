"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import calendar
import os

import datetime

from src.com.jalasoft.search_files.search import asset
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER
from src.com.jalasoft.search_files.utils import utils
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria


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
        if not search_criteria.get_search_filter()['advance_flag']:
            return self.basic_results(search_criteria)
        else:
            pass

    def filtering_by_date(self, search_criteria):
        file_name = search_criteria.get_search_filter()
        init_date = file_name['init_date'].split('/')
        end_date = file_name['end_date'].split('/')
        epoch_time_var = utils.convert_to_epoch_time(int(init_date[0]), int (init_date[1]), int(init_date[2]))
        end_epoch_time_var = utils.convert_to_epoch_time(int(end_date[0]), int(end_date[1]), int(end_date[2]))
        return self.advanced_search_by_creation_time(search_criteria, epoch_time_var, end_epoch_time_var)

    def basic_results(self, search_criteria):
        list_of_found = []
        list_from_path = self.print_directory()
        file_name = search_criteria.get_search_filter()
        for result in list_from_path:
            if file_name['file_name'] in os.path.basename(result.get_file_name()):
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found

    def advanced_search_by_creation_time(self, search_criteria, start_date, end_date):
        list_of_found = []
        list_from_path = self.print_directory()
        file_name = search_criteria.get_search_filter()
        for result in list_from_path:
            if start_date <= result.get_creation_time() <= end_date \
                    and file_name['file_name'] in os.path.basename(result.get_file_name()):
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found



# search_criteria = SearchCriteria()
# search_criteria.set_search_filter({"advance_flag": False,
#                                    "criteria": 1,
#                                    "path": 'D:\\',
#                                    "size": None,
#                                    "init_date": '2018/01/11',
#                                    "end_date": '2018/01/30',
#                                    "extension": None,
#                                    "file_name": 'Franco',
#                                    "directory_name": None,
#                                    "hidden": None})
#
# search = Search(search_criteria)
# listM = search.filtering_by_date(search_criteria)
# for value in listM:
#     print(value.get_file_name())
#     print("File Size: %s Mbytes" % str(int(value.get_file_size())/1000000))
#     print("creation date: %s" % value.get_creation_time())
# print('hi')
# print(os.path.basename('D:\MauricioZ\Documments\Courses\Dev Fundamentals\module_2\SearchFiles_77\\test\mauricio.txt'))
