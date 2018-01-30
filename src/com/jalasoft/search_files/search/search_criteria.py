"""
This module will contain the main criteria for a specific search
"""
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

class Search_Criteria(object):
    """
     This class contains the methods that will be used to search.
    """

    def __init__(self, criteria=3, path='/', advanced_search=False):
        """
        This method is the constructor of the search criteria.
        :param criteria: Type of search.                                     type: int.
        :param path: A path where the search will be made.                   type: string.
        :param advanced_search: Determine the type of search.                type: boolean.
        """


        self.basic_search = {
            "criteria": criteria,
            "path": path,
        }

        if advanced_search:
            self.advance_search = {
                "criteria": criteria,
                "path": path,
                "size": None,
                "date": None,
                "extension": None,
                "file_name": None,
                "directory_name": None,
                "hidden": None
            }
            LOGGER.info("valid advance search is created".format(self.advance_search))
        LOGGER.info("valid basic search is created".format(self.basic_search))

    def get_basic_criteria(self):
        """
        This method return the basic criteria.
        :return: dictionary.
        """
        return self.basic_search

    def get_advance_criteria(self,):
        """
        This method returns the advance criteria.
        :return: dictionary.
        """
        return self.advance_search

    def set_advanced_search_filters(self, filter_dictionary):
        """
        This method set the advance search dictionary.
        :param filter_dictionary: The dictionary that will modify the one from the class.
        :return: None
        """
        self.advance_search.update(filter_dictionary)

    def set_basic_search_filters(self, filter_dictionary):
        """
        This method set the basic search dictionary.
        :param filter_dictionary: The dictionary that will modify the one from the class.
        :return: None
        """
        self.basic_search.update(filter_dictionary)
