"""
class for unit tests
"""
import pytest
import os
from SearchFiles_77.src.com.jalasoft.search_files.search.search_engine import Search

@pytest.mark.search
def test_a_search_is_created_without_parameters():
    """
    testing that search object is being created
    :return:
    """
    search_engine = Search()
    assert isinstance(search_engine, Search)


@pytest.mark.search
def test_a_search_is_created_with_path_list_files_in_the_given_path():
    """

    :return:
    """
    search_path = os.getcwd()
    search_engine = Search(path_file=search_path)
    assert isinstance(search_engine, Search)
    assert search_engine.print_directory() is not None
