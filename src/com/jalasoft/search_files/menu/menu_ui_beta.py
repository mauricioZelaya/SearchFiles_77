"""
Menu test
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk


class SearchMenu:
    """
    Start menu
    """

    def __init__(self):
        """
        Start menu
        """

        self.main = Tk()

        self.main.title("Menu Search")
        self.main.option_add("*Font", "Helvetica 12")
        self.main.minsize(400, 300)

        self.text_menu = Label(self.main, text="Add Path and Key Name")
        self.text_menu.grid(column=2)

        self.text_path = Label(self.main, text="Path :")
        self.text_path.grid(row=2, column=1)
        self.path_str = StringVar()
        self.path_entry = Entry(self.main, textvariable=self.path_str)
        self.path_entry.grid(row=2, column=2)

        self.text_key = Label(self.main, text="Key Name :")
        self.text_key.grid(row=3, column=1)
        self.key_str = StringVar()
        self.key_entry = Entry(self.main, textvariable=self.key_str)
        self.key_entry.grid(row=3, column=2)

        self.search = Button(self.main, text="Search", command=self.b_search)
        self.search.grid(row=6, column=2)

        self.cancel = Button(self.main, text="Cancel", command=self.b_quit)
        self.cancel.grid(row=7, column=2)

        self.listbox = Listbox(self.main)
        self.listbox.grid(row=0, column=0)

        self.main.mainloop()

    def b_quit(self):
        """
        exit of application
        """
        self.main.destroy()

    def b_search(self):
        """
        search of application
        """
        get_path = self.path_str.get()
        get_key = self.key_str.get()
        self.listbox.insert(END, get_path, get_key)




if __name__ == '__main__':
    SearchMenu()