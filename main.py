import tkinter as tk

from src.com.jalasoft.search_files.menu.menu_ui import SearchMenu
from src.com.jalasoft.search_files.utils.logging import LOGGER as LOGGER

def main():
    hidden = True
    modification_date = True
    creation_date = True
    last_date = True
    error = True
    root = tk.Tk()
    SearchMenu(root, hidden, modification_date, creation_date, last_date, error)
    root.mainloop()


if __name__ == '__main__':
    LOGGER.info("starting application START")
    main()
    LOGGER.info("starting application START")