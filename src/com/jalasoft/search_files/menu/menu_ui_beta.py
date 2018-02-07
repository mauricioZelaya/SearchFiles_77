"""
Menu test
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys

import time

from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria


class SearchMenu:
    """
    Start menu
    """

    def __init__(self):
        """
        Start menu
        """

        self._search_criteria = SearchCriteria()
        self.search_obj = Search(self._search_criteria)

        self.main = Tk()

        self.main.title("Menu Search")
        self.main.option_add("*Font", "Helvetica 12")
        # self.main.attributes('-fullscreen', True)

        self.text_menu = Label(self.main, text="Add Path and Key Name")
        self.text_menu.grid(row=1, column=2)

        self.text_path = Label(self.main, text="Path :")
        self.text_path.grid(row=2, column=1)
        self.path_str = StringVar()
        self.path_entry = Entry(self.main, textvariable=self.path_str, width=40)
        self.path_entry.grid(row=2, column=2)

        self.text_key = Label(self.main, text="Key Name :")
        self.text_key.grid(row=3, column=1)
        self.key_str = StringVar()
        self.key_entry = Entry(self.main, textvariable=self.key_str, width=40)
        self.key_entry.grid(row=3, column=2)

        self.search = Button(self.main, text="Search", command=self.b_search)
        self.search.grid(row=4, column=1, padx=20, pady=0)

        self.cancel = Button(self.main, text="Cancel", command=self.b_quit)
        self.cancel.grid(row=4, column=2, padx=0, pady=10)

        self.path = Button(self.main, text="Select Path", command=self.set_path)
        self.path.grid(row=2, column=3)

        self.listbox = Listbox(self.main, width=70, height=10, bg='white')
        self.listbox.grid(row=5, column=3)

        self.advance = ttk.Checkbutton(self.main, text="Advance", variable=None, onvalue=True)
        self.advance.grid(row=5, column=1)

        # self.can1 = Canvas(self.main, width=1000, height=500, bg='white')
        # self.can1.grid(row=4, column=2)

        self.main.mainloop()

    def b_quit(self):
        """
        exit of application
        """
        self.main.destroy()

    def set_path(self):
        """
        select a path
        """
        pass

    def b_search(self):
        """
        search of application
        """
        get_path = self.path_str.get()
        get_key = self.key_str.get()

        is_valid_path = utils.is_a_valid_path(get_path)
        if is_valid_path["valid"]:
            self._search_criteria.set_search_filter({'path': get_path})

        else:
            print(is_valid_path["message"])
        self._search_criteria.set_search_filter({"file_name": get_key})
        list_d = self.search_obj.create_list_of_ocurrences(self._search_criteria)

        for value in list_d:
            self.listbox.insert(END, "----------------------------------------------------------------------")
            self.listbox.insert(END, value.get_file_name())
            if not value.get_is_directory():
                self.listbox.insert(END, "File Size: %s Mbytes" % str(int(value.get_file_size())/1000000))
                self.listbox.insert(END, "creation date: %s" % time.asctime(time.localtime(value.get_creation_time())))
                self.listbox.insert(END, "last modification date: %s" % time.asctime(time.localtime(value.get_last_modification_date())))
                self.listbox.insert(END, "last access date: %s" % time.asctime(time.localtime(value.get_last_access_time())))
                self.listbox.insert(END, "---------------------------------------------------------------------------")
        self.listbox.insert(END, "Total files matched: %s" % self.search_obj.get_total_matches())


if __name__ == '__main__':
    SearchMenu()