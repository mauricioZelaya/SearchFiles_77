"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import os

# from src.com.jalasoft.search_files.search.asset import Asset
from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.folder import Folder
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER
from src.com.jalasoft.search_files.utils import utils


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

        LOGGER.info("getting all the directories and files from path START")
        for root, dirs, files in os.walk(search_criteria_values['path'], topdown=False):
            if search_criteria_values['criteria'] == 2 or search_criteria_values['criteria'] == 3:
                for value in dirs:
                    directory = Folder()
                    directory.set_file_name(os.path.join(root, value))
                    directory.set_is_directory(True)
                    list_dir.append(directory)
            if search_criteria_values['criteria'] == 1 or search_criteria_values['criteria'] == 3:
                for value in files:
                    file_name = os.path.join(root, value)
                    file = File()
                    file.set_file_name(file_name)
                    file.set_is_directory(False)
                    file.set_file_size(os.path.getsize(file_name))
                    list_dir.append(file)
        LOGGER.info("getting all the directories and files from path START")
        return list_dir

    def create_list_of_ocurrences(self, search_criteria):
        """

        :return:
        """
        basic_result_list = self.basic_results(search_criteria.get_search_filter()['file_name'])
        if not search_criteria.get_search_filter()['advance_flag']:
            return basic_result_list
        else:
            return self.verify_advanced_filters(search_criteria, basic_result_list)

    def basic_results(self, file_keyword):
        """
        method to find all the ocurrences without filters of a search
        :param file_keyword: word to search in the given file path
        :return: a list of all ocurrences of keyword in file path
        """
        list_of_found = []
        list_from_path = self.print_directory()
        for result in list_from_path:
            if file_keyword in os.path.basename(result.get_file_name()):
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found

    def verify_advanced_filters(self, search_criteria, basic_result_list):
        """
        this method will be used to filter results of the search according the filters set
        :param search_criteria: advanced filters for the search
        :return:
        """
        filter_list = search_criteria.get_search_filter()
        basic_search_result_list = basic_result_list
        if not filter_list['start_creation_date'] is None and not filter_list['end_creation_date'] is None:
            start_creation_date = filter_list['start_creation_date']
            end_creation_date = filter_list['end_creation_date']
            basic_search_result_list = self.advanced_search_by_creation_time(basic_search_result_list,
                                                                             utils.date_to_epoch_time(
                                                                                 start_creation_date)
                                                                             ,
                                                                             utils.date_to_epoch_time(end_creation_date)
                                                                             )

        if not filter_list['start_modification_date'] is None and not filter_list['end_modification_date'] is None:
            start_modification_date = filter_list['start_modification_date']
            end_modification_date = filter_list['end_modification_date']
            basic_search_result_list = self.advanced_search_by_modification_time(basic_search_result_list,
                                                                             utils.date_to_epoch_time(
                                                                                 start_modification_date)
                                                                             ,
                                                                             utils.date_to_epoch_time(end_modification_date)
                                                                             )
        return basic_search_result_list

    def advanced_search_by_creation_time(self, basic_search_result_list, start_date, end_date):
        """
        this method will create a list of results according the creation date
        :param basic_search_result_list:
        :param start_date:
        :param end_date:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result in basic_search_result_list:
            if start_date <= result.get_creation_time() <= end_date:
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found

    def advanced_search_by_modification_time(self, basic_search_result_list, start_date, end_date):
        """
        this method will create a list of results according the modification date
        :param basic_search_result_list:
        :param start_date:
        :param end_date:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result in basic_search_result_list:
            if start_date <= result.get_last_modification_date() <= end_date:
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found


# search_criteria = SearchCriteria()
# search_criteria.set_search_filter({"advance_flag": True,
#                                    "criteria": 1,
#                                    "path": 'D:\\',
#                                    "size": None,
#                                    "start_creation_date": None,
#                                    "end_creation_date": None,
#                                    "start_modification_date": '2018/01/13',
#                                    "end_modification_date": '2018/01/30',
#                                    "start_last_access_date": None,
#                                    "end_last_access_date": None,
#                                    "extension": None,
#                                    "file_name": 'Franco',
#                                    "directory_name": None,
#                                    "hidden": None})
#
# search = Search(search_criteria)
# listM = search.create_list_of_ocurrences(search_criteria)
# for value in listM:
#     print(value.get_file_name())
#     print("File Size: %s Mbytes" % str(int(value.get_file_size()) / 1000000))
#     print("creation date: %s" % time.asctime(time.localtime(value.get_creation_time())))
# print('hi')
# print(os.path.basename('D:\MauricioZ\Documments\Courses\Dev Fundamentals\module_2\SearchFiles_77\\test\mauricio.txt'))
