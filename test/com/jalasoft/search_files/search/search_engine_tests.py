"""
class for unit tests
"""
import os
import pytest
from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria



@pytest.mark.search_engine
def test_a_search_is_created_withempty_search_criteria():
    """
    testing that search object is being created
    :return:
    """
    search_criteria = SearchCriteria()
    search_engine = Search(search_criteria)
    assert isinstance(search_engine, Search)


@pytest.mark.search_engine
def test_a_search_is_created_with_search_criteria_with_a_path():
    """
    testing that search object is being created with a specific path in search criteria object set
    :return:
    """
    search_path = os.getcwd()
    search_criteria = SearchCriteria(search_path)
    search_engine = Search(search_criteria)
    assert isinstance(search_engine, Search)
    assert search_engine.print_directory() is not None


@pytest.mark.search_engine
def test_given_a_keyword_a_basic_search_is_performed():
    pass