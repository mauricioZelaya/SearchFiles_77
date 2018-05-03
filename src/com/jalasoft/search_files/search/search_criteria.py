"""
This module will contain the main criteria for a specific search
"""
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER



class SearchCriteria(object):
    """
     This class contains the methods that will be used to search.
    """

    def __init__(self, criteria=3, path='/'):
        """
        This method is the constructor of the search criteria.
        :param criteria: Type of search.                                     type: int.
        :param path: A path where the search will be made.                   type: string.
        """

        self._search_filter = {
            "advance_flag": False,
            "criteria": criteria,
            "path": path,
            "size": None,
            "creation_date": {"start_date": None, "end_date": None},
            "modification_date": {"start_date": None, "end_date": None},
            "last_access_date": {"start_date": None, "end_date": None},
            "extension": None,
            "file_name": None,
            "directory_name": None,
            "owner_name": None,
            "text_value": None
        }
        LOGGER.info("valid search filter dictionary was created: {}".format(self._search_filter))

    def get_search_filter(self):
        """
        This method returns the advance criteria.
        :return: dictionary.
        """
        LOGGER.info("search filter was returned")
        return self._search_filter


    def set_search_filter(self, filter_dictionary):
        """
        This method set the advance search dictionary.
        :param filter_dictionary: The dictionary that will modify the one from the class.
        :return: None
        """
        self._search_filter.update(filter_dictionary)
        LOGGER.info("search filter was updated")


    def get_advance_flag(self):
        """
        This method returns the flag that determine if the search is a basic or an advance one.
        :return: Boolean.
        """
        LOGGER.info("advance flag was returned")
        return self._search_filter["_advance_flag"]
