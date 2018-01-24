import sys

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.choices = {
                "1": self.set_search_path,
                "2": self.set_search_file_name,
                "3": self.set_filters,
                "4": self.quit
                }

    def display_menu(self):
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
        print("search path")


    def set_search_file_name(self):
        print("search file name")


    def set_filters(self):
        print("search filters")


    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()