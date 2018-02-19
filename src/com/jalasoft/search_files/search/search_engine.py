"""
class Search_Engine perform the search on a given path of a given file_name applying
all the desired filters
"""
import os

import filetype

from src.com.jalasoft.search_files.search.file import File
from src.com.jalasoft.search_files.search.folder import Folder
from src.com.jalasoft.search_files.utils import utils
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
                    file.set_file_owner_name(utils.get_file_owner(file_name))
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
                kind = filetype.guess(result.get_file_name())
                if kind is not None:
                    result.set_file_type(kind.mime)
                else:
                    result.set_file_type('unknown')
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
        if not filter_list['creation_date']['start_date'] is None and not \
                filter_list['creation_date']['end_date'] is None:
            start_creation_date = filter_list['creation_date']['start_date']
            end_creation_date = filter_list['creation_date']['end_date']
            basic_search_result_list = self.advanced_search_by_creation_time(basic_search_result_list,
                                                                             utils.date_to_epoch_time(
                                                                                 start_creation_date)
                                                                             ,
                                                                             utils.date_to_epoch_time(end_creation_date)
                                                                             )

        if not filter_list['modification_date']['start_date'] is None and not \
                filter_list['modification_date']['end_date'] is None:
            start_modification_date = filter_list['modification_date']['start_date']
            end_modification_date = filter_list['modification_date']['end_date']
            basic_search_result_list = self.advanced_search_by_modification_time(basic_search_result_list,
                                                                                 utils.date_to_epoch_time
                                                                                 (start_modification_date),
                                                                                 utils.date_to_epoch_time
                                                                                 (end_modification_date))

        if not filter_list['last_access_date']['start_date'] is None and not \
                filter_list['last_access_date']['end_date'] is None:
            start_modification_date = filter_list['last_access_date']['start_date']
            end_modification_date = filter_list['last_access_date']['end_date']
            basic_search_result_list = self.advanced_search_by_last_access_date(basic_search_result_list,
                                                                                utils.date_to_epoch_time
                                                                                (start_modification_date),
                                                                                utils.date_to_epoch_time
                                                                                (end_modification_date))

        if not filter_list['owner_name'] is None:
            basic_search_result_list = self.advanced_search_by_owner(basic_search_result_list,
                                                                     filter_list['owner_name'])

        if not filter_list['size'] is None:
            basic_search_result_list = self.advanced_search_by_size(basic_search_result_list, filter_list['size'])

        if not filter_list['text_value'] is None:
            basic_search_result_list = self.advanced_search_content_in_file(basic_search_result_list,
                                                                            filter_list['text_value'])

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

    def advanced_search_by_last_access_date(self, basic_search_result_list, start_date, end_date):
        """
        this method will create a list of results according the last access date
        :param basic_search_result_list:
        :param start_date:
        :param end_date:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result in basic_search_result_list:
            if start_date <= result.get_last_access_time() <= end_date:
                list_of_found.append(result)
                self._total_of_matches += 1
        return list_of_found

    def advanced_search_by_owner(self, basic_search_result_list, file_owner_to_search):
        """

        :param basic_search_result_list:
        :param file_owner_to_search:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result_in_basic_search in basic_search_result_list:
            if result_in_basic_search.get_file_owner_name() == file_owner_to_search:
                list_of_found.append(result_in_basic_search)
                self._total_of_matches += 1
        return list_of_found

    def advanced_search_by_size(self, basic_search_result_list, file_size_criteria):
        """

        :param basic_search_result_list:
        :param file_size_criteria:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result_in_basic_search in basic_search_result_list:
            if file_size_criteria == '<10' and result_in_basic_search.get_file_size() >=0 \
                    and result_in_basic_search.get_file_size() <= 1000000:
                list_of_found.append(result_in_basic_search)
                self._total_of_matches += 1
            elif file_size_criteria == '<100' and result_in_basic_search.get_file_size() > 1000000 \
                    and result_in_basic_search.get_file_size() <= 100000000:
                list_of_found.append(result_in_basic_search)
                self._total_of_matches += 1
            elif file_size_criteria == '>100' and result_in_basic_search.get_file_size() > 100000000:
                list_of_found.append(result_in_basic_search)
                self._total_of_matches += 1

        return list_of_found

    def advanced_search_content_in_file(self, basic_search_result_list, text_in_file):
        """

        :param basic_search_result_list:
        :param text_in_file:
        :return:
        """
        list_of_found = []
        self._total_of_matches = 0
        for result_in_basic_search in basic_search_result_list:
            file_content = utils.get_file_content(result_in_basic_search.get_file_name())
            if text_in_file in file_content:
                list_of_found.append(result_in_basic_search)
                self._total_of_matches += 1

        return list_of_found




