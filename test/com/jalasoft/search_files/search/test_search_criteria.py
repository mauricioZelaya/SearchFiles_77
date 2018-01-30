"""
This module contain the test for the module search_criteria.py
"""

import pytest
import src.com.jalasoft.search_files.search.search_criteria as sc
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

@pytest.mark.search_criteria
def test_is_basic_search_criteria_instance():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")

    criteria = sc.Search_Criteria()
    basic_search = criteria.get_basic_criteria()
    LOGGER.info("the basic filter is equals to: ".format(basic_search))
    assert isinstance(criteria, sc.Search_Criteria)

    LOGGER.info("=========test_is_search_criteria_instance has PASSED=========")

@pytest.mark.search_criteria
def test_is_advance_search_criteria_instance():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")


    criteria = sc.Search_Criteria(advanced_search=True)
    advanced_search = criteria.get_advance_criteria()
    LOGGER.info("the advanced filter is equals to: ".format(advanced_search))
    assert isinstance(criteria, sc.Search_Criteria)

    LOGGER.info("=========test_is_search_criteriainstance has PASSED=========")

@pytest.mark.search_criteria
def test_set_advanced_search_filters():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")


    criteria = sc.Search_Criteria(advanced_search=True)
    search_criteria = {
                "criteria": 3,
                "path": "/",
                "size": 55,
                "date": 2018,
                "extension": ".jpg",
                "file_name": "file",
                "directory_name": "Dir",
                }

    old_search_criteria = criteria.get_advance_criteria()
    new_search_criteria = criteria.set_advanced_search_filters(search_criteria)
    assert old_search_criteria != new_search_criteria

    LOGGER.info("=========test_is_search_criteriainstance has PASSED=========")

@pytest.mark.search_criteria
def test_set_advanced_search_filters_only_some_values():
    """
    This method verify that the instance is created
    :return: None
    """
    LOGGER.info("=========test_is_search_criteria_instance is starting=========")


    search_criteria = sc.Search_Criteria(advanced_search=True)
    expected_criteria = {
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
    search_criteria.set_advanced_search_filters(filters_to_modify)
    assert expected_criteria == search_criteria.get_advance_criteria()

    LOGGER.info("=========test_is_search_criteriainstance has PASSED=========")
