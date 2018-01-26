"""
class for unit tests
"""
import pytest
import os
from src.com.jalasoft.search_files.search.search_engine import Search

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


@pytest.mark.search
def test_a_path_is_modified_with_a_given_path():
    """

    :return:
    """
    search_engine = Search()
    search_path = os.getcwd()
    search_engine.set_path(search_path)
    assert search_engine.get_path() == search_path

@pytest.mark.search
def test_a_file_name_is_modified_with_given_new_file_name():
    """

    :return:
    """
    search_engine = Search(file_name='file_name')
    new_file = 'new_search'
    search_engine.set_file_name(new_file)
    assert search_engine.get_file_name() == new_file
