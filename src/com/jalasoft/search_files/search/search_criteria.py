"""
This module will contain the main criteria for a specific search
"""
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

class SearchCriteria(object):
    """
     This class contains the methods that will be used to search.
    """

    def __init__(self, criteria=3, path='/', advanced_flag=False):
        """
        This method is the constructor of the search criteria.
        :param criteria: Type of search.                                     type: int.
        :param path: A path where the search will be made.                   type: string.
        :param advanced_flag: Determine the type of search.                  type: boolean.
        """

        self._advance_flag = advanced_flag

        if self._advance_flag:
            self._advance_search = {
                "criteria": criteria,
                "path": path,
                "size": None,
                "date": None,
                "extension": None,
                "file_name": None,
                "directory_name": None,
                "hidden": None
            }
            LOGGER.info("valid advance search is created: {}".format(self._advance_search))

        else:
            self._basic_search = {
                "criteria": criteria,
                "path": path,
            }
            LOGGER.info("valid basic search is created: {}".format(self._basic_search))

    def get_basic_search(self):
        """
        This method return the basic criteria.
        :return: dictionary.
        """
        return self._basic_search

    def get_advance_search(self,):
        """
        This method returns the advance criteria.
        :return: dictionary.
        """
        return self._advance_search

    def set_advanced_search_filters(self, filter_dictionary):
        """
        This method set the advance search dictionary.
        :param filter_dictionary: The dictionary that will modify the one from the class.
        :return: None
        """
        self._advance_search.update(filter_dictionary)

    def set_basic_search_filters(self, filter_dictionary):
        """
        This method set the basic search dictionary.
        :param filter_dictionary: The dictionary that will modify the one from the class.
        :return: None
        """
        self._basic_search.update(filter_dictionary)

    def get_advance_flag(self):
        """
        This method returns the flag that determine if the search is a basic or an advance one.
        :return: Boolean.
        """
        return self._advance_flag
