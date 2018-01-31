"""
class Menu displays the all options to search a file, path, archive
"""
import sys

import time

from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.choices = {"1": self.set_search_path, "2": self.set_filters,
                        "3": self.set_search_file_name, "4": self.quit}
        self.submenu_choices = {"1": self.search_folder, "2": self.search_file, "3": self.search_folder_file,
                                "4": self.back_menu}
        self._search_criteria = SearchCriteria()
        self.search_obj = Search(self._search_criteria)

    def display_menu(self):
        """
        Menu that will be displayed.
        """
        print("""
            Search Menu
            1. Set Path
            2. Set Filters
            3. Search by Name
            4. Quit
            """)

    def display_sub_menu_filter(self):
        """
        Sub Menu for filter option that will be displayed.
        """
        print("""
            Menu Filters
            1. Folders Only
            2. Files Only
            3. Folders and Files
            4. Back Menu
            """)

    def run(self):
        """
        Display the menu and respond to choices.
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def run_sub_menu_filter(self):
        """
        Display the sub menu for filter and respond to choices.
        """
        while True:
            self.display_sub_menu_filter()
            sub_choice = input("Enter an option: ")
            action = self.submenu_choices.get(sub_choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(sub_choice))

    def set_search_path(self):
        """
        Display the all files into a determinate path.
        """
        print("Set Path")
        path = input("Insert a root path: ")
        print(path)
        is_valid_path = utils.is_a_valid_path(path)
        if is_valid_path["valid"]:
            self._search_criteria.set_basic_search_filters({'path': path})
        else:
            print(is_valid_path["message"])

    def set_search_file_name(self):
        """
        Display a determinate file.
        """
        file_name = input("Set File Name: ")
        self._search_criteria.set_basic_search_filters({"file_name": file_name})
        list_d = self.search_obj.create_list_of_ocurrences(self._search_criteria)
        for value in list_d:
            print("---------------------------------------------------------------------------")
            print(value.get_file_name())
            if not value.get_is_directory():
                print("File Size: %s Mbytes" % str(int(value.get_file_size())/1000000))
                print("creation date: %s" % time.asctime(time.localtime(value.get_creation_time())))
                print("last modification date: %s" % time.asctime(time.localtime(value.get_last_modification_date())))
                print("last access date: %s" % time.asctime(time.localtime(value.get_last_access_time())))
                print("---------------------------------------------------------------------------")
        print("Total files matched: %s" % self.search_obj.get_total_matches())

    def set_filters(self):
        """
        Display some filters to search.
        """
        self.run_sub_menu_filter()

    def search_folder(self):
        """
        Display a determinate folder.
        """
        self._search_criteria.set_basic_search_filters({'criteria': 2})
        self.run()

    def search_file(self):
        """
        Display a determinate file.
        """
        self._search_criteria.set_basic_search_filters({'criteria': 1})
        self.run()

    def search_folder_file(self):
        """
        Display a determinate file or folder.
        """
        self._search_criteria.set_basic_search_filters({'criteria': 3})
        self.run()

    def back_menu(self):
        """
        Return to Menu.
        """
        self.run()

    def quit(self):
        """
        End program.
        """
        print("Thank you for using search today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
