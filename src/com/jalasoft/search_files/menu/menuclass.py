"""
class Menu displays the all options to search a file, path, archive
"""
import sys
from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.choices = {"1": self.set_search_path, "2": self.set_search_file_name,
                        "3": self.set_filters, "4": self.quit}
        self.submenu_choices = {"1": self.search_folder, "2": self.search_file, "3": self.search_folder_file,
                                "4": self.back_menu}
        self.search_obj = Search()

    def display_menu(self):
        """
        Menu that will be displayed.
        """
        print("""
            Search Menu
            1. Search Path
            2. Search File Name
            3. Search Filter
            4. Quit
            """)

    def display_sub_menu_filter(self):
        """
        Sub Menu for filter option that will be displayed.
        """
        print("""
            Search Menu Filter
            1. Search Folder
            2. Search File
            3. Search Folder and File
            4. Return Menu
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
        print("search path")
        path = input("Insert a root path: ")
        print(path)
        is_valid_path = utils.is_a_valid_path(path)
        if is_valid_path["valid"]:
            self.search_obj.set_path(path)
            list_d = self.search_obj.print_directory()
            for value in list_d:
                print(value.get_file_name())
        else:
            print(is_valid_path["message"])

    def set_search_file_name(self):
        """
        Display a determinate file.
        """
        print("search file")

    def set_filters(self):
        """
        Display some filters to search.
        """
        self.run_sub_menu_filter()

    def search_folder(self):
        """
        Display a determinate folder.
        """
        print("Search Folder")

    def search_file(self):
        """
        Display a determinate file.
        """
        print("Search File")

    def search_folder_file(self):
        """
        Display a determinate file or folder.
        """
        print("Search File or Folder")

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
