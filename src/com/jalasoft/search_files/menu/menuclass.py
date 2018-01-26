"""
class Menu displays the all options to search a file, path, archive
"""
import sys
from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search


class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.choices = {"1": self.set_search_path, "2": self.set_search_file_name,
                        "3": self.set_filters, "4": self.quit}
        self.search_obj = Search()

    def display_menu(self):
        """Menu that will be displayed."""
        print("""
            Search Menu
            1. set search path
            2. set search file name
            3. set filters
            4. Quit
            """)

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def set_search_path(self):
        """Display the all files into a determinate path."""
        print("search path")
        path = input("Insert a root path")
        print(path)
        is_valid_path = utils.is_a_valid_path(path)
        if (is_valid_path):
            self.search_obj.set_path(path)
            list_d = self.search_obj.print_directory()
            print('\n'.join(list_d))
        else:
            print(is_valid_path["message"])

    def set_search_file_name(self):
        """Display a determinate file."""

        print("search file name")

    def set_filters(self):
        """Display some filters to search."""
        print("search filters")

    def quit(self):
        """End program."""
        print("Thank you for using search today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
