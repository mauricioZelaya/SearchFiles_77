"""
This module contain the test for the module search_criteria.py
"""

import pytest
import src.com.jalasoft.search_files.search.search_criteria as sc
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

@pytest.mark.search_criteria
def test_is_filter_search_criteria_instance():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_filter_search_criteria_instance is starting=========")

    criteria = sc.SearchCriteria()
    search_filter = criteria.get_search_filter()
    LOGGER.info("the search filter is equals to: {}".format(search_filter))
    assert isinstance(criteria, sc.SearchCriteria)

    LOGGER.info("=========test_is_filter_search_criteria_instance has PASSED=========")


@pytest.mark.search_criteria
def test_set_search_filters():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")

    criteria = sc.SearchCriteria()
    search_criteria = {
        "advance_flag":False,
        "criteria": 3,
        "path": "/",
        "size": 55,
        "date": 2018,
        "extension": ".jpg",
        "file_name": "file",
        "directory_name": "Dir",
    }

    old_search_criteria = criteria.get_search_filter()
    new_search_criteria = criteria.set_search_filter(search_criteria)
    assert old_search_criteria != new_search_criteria

    LOGGER.info("=========test_is_search_criteria_instance has PASSED=========")


@pytest.mark.search_criteria
def test_set_search_filters_only_some_values():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")

    search_criteria = sc.SearchCriteria()
    expected_criteria = {
        "advance_flag":False,
        "criteria": 3,
        "path": "/",
        "size": None,
        "date": 2018,
        "extension": None,
        "file_name": "file",
        "directory_name": None,
        "hidden": None
    }

    filters_to_modify = {
        "size": None,
        "date": 2018,
        "file_name": "file",
        "directory_name": None,
        "hidden": None
    }
    search_criteria.set_search_filter(filters_to_modify)
    assert expected_criteria == search_criteria.get_search_filter()

    LOGGER.info("=========test_is_search_criteria_instance has PASSED=========")
