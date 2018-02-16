"""
Menu UI
"""

import tkinter as tk
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

import time

from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
from src.com.jalasoft.search_files.utils import utils


class SearchMenu(tk.Frame):
    """
    Start menu
    """
    def __init__(self, parent, hidden, creation_date, modification_date, last_date, error):
        """
        Start menu
        """
        self.master = parent
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.last_date = last_date
        self.hidden = hidden
        self.error = error
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()
        self._search_criteria = SearchCriteria()
        self.search_obj = Search(self._search_criteria)

    def configure_gui(self):
        """
        UI configuration
        """
        self.master.title('Menu Search')
        self.master.configure(width=1432, height=700)

    def create_widgets(self):
        """
        Display all UI
        """
        self.create_labels()
        self.create_textbox()
        self.create_buttons()
        self.create_checkbox()
        # self.create_listbox()
        self.result_of_search()

    def create_labels(self):
        """
        all Labels
        """
        self.text_menu = tk.Label(self.master, text="Add Path and Key Name")
        self.text_menu.place(x=10, y=10)
        self.text_path = tk.Label(self.master, text="Path :")
        self.text_path.place(x=10, y=40)
        self.text_key = tk.Label(self.master, text="Key Name :")
        self.text_key.place(x=10, y=75)

    def create_textbox(self):
        """
        all Textbox
        """
        self.path_str = tk.StringVar()
        self.path_entry = tk.Entry(self.master, textvariable=self.path_str, width=30, state='disabled')
        self.path_entry.place(x=90, y=40)
        self.key_str = tk.StringVar()
        self.key_entry = tk.Entry(self.master, textvariable=self.key_str, width=30)
        self.key_entry.place(x=90, y=75)

    def create_buttons(self):
        """
        all buttons
        """
        self.search = tk.Button(self.master, text="Search", command=self.search_criteria)
        self.search.place(x=200, y=100)
        self.cancel = tk.Button(self.master, text="Cancel", command=self.exit_application)
        self.cancel.place(x=270, y=100)
        self.path = tk.Button(self.master, text="Select Path", command=self.select_path_from_button)
        self.path.place(x=350, y=40)

    def create_listbox(self):
        """
        all Labels
        """
        self.listbox = tk.Listbox(self.master, width=41, height=30, bg='white')
        self.listbox.place(x=10, y=140)

    def create_checkbox(self):
        """
        all buttons
        """
        self.advanced = tk.Checkbutton(self.master, text="Advanced", variable=None, onvalue=True,
                                       command=self.hidden_with_checkbox)
        self.advanced.place(x=350, y=100)

    def select_creation_date_button(self):
        """
        all Labels
        """
        self.create_date = tk.Button(self.master, text="Creation day: ", command=self.enable_creation_date)
        self.create_date.place(x=470, y=10)

    def select_modification_date_button(self):
        """
        all Labels
        """
        self.modify_date = tk.Button(self.master, text="Modification day: ", command=self.enable_modification_date)
        self.modify_date.place(x=730, y=10)

    def select_last_date_button(self):
        """
        all Labels
        """
        self.the_last_date = tk.Button(self.master, text="Last Access day: ", command=self.enable_last_date)
        self.the_last_date.place(x=990, y=10)

    def hidden_labels(self):
        """
        all Labels
        """
        self.text_start_date = tk.Label(self.master, text="Start Date")
        self.text_start_date.place(x=470, y=42)
        self.text_end_date = tk.Label(self.master, text="End Date")
        self.text_end_date.place(x=595, y=42)

    def hidden_labels_modification_date(self):
        """
        all Labels
        """
        self.text_start_date_modify = tk.Label(self.master, text="Start Date")
        self.text_start_date_modify.place(x=730, y=42)
        self.text_end_date_modify = tk.Label(self.master, text="End Date")
        self.text_end_date_modify.place(x=855, y=42)

    def hidden_labels_last_date(self):
        """
        all Labels
        """
        self.text_start_date_last = tk.Label(self.master, text="Start Date")
        self.text_start_date_last.place(x=990, y=42)
        self.text_end_date_last = tk.Label(self.master, text="End Date")
        self.text_end_date_last.place(x=1115, y=42)

    def hidden_creation_date(self):
        """
        all Labels
        """
        self.create_date_value = tk.StringVar()
        self.creation_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                            borderwidth=2, textvariable=self.create_date_value)
        self.creation_cal_start.place(x=470, y=65)
        self.create_date_end_value = tk.StringVar()
        self.creation_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                          borderwidth=2, textvariable=self.create_date_end_value)
        self.creation_cal_end.place(x=595, y=65)

    def hidden_modification_date(self):
        """
        all Labels
        """
        self.modification_date_value = tk.StringVar()
        self.modification_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                                borderwidth=2, textvariable=self.modification_date_value)
        self.modification_cal_start.place(x=730, y=65)
        self.modification_date_end_value = tk.StringVar()
        self.modification_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                              borderwidth=2, textvariable=self.modification_date_end_value)
        self.modification_cal_end.place(x=855, y=65)

    def hidden_last_date(self):
        """
        all Labels
        """
        self.last_date_value = tk.StringVar()
        self.last_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                        borderwidth=2, textvariable=self.last_date_value)
        self.last_cal_start.place(x=990, y=65)
        self.last_date_end_value = tk.StringVar()
        self.last_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                      borderwidth=2, textvariable=self.last_date_value)
        self.last_cal_end.place(x=1115, y=65)

    def hidden_size_radiobutton(self):
        """
        all Labels
        """
        self.text_size = tk.Label(self.master, text="Size")
        self.text_size.place(x=470, y=90)
        self.var = tk.IntVar()
        self.radio_one = tk.Radiobutton(self.master, text="0 to 10 Mb", variable=self.var, value=1, command=None)
        self.radio_one.place(x=470, y=110)
        self.radio_two = tk.Radiobutton(self.master, text="11 to 100 Mb", variable=self.var, value=2, command=None)
        self.radio_two.place(x=470, y=130)
        self.radio_three = tk.Radiobutton(self.master, text="Greater than 101 Mb", variable=self.var, value=3,
                                          command=None)
        self.radio_three.place(x=470, y=150)

    def hidden_word_in_file(self):
        """
        all Labels
        """
        self.text_world_in_file = tk.Label(self.master, text="Word in file (only text files: )")
        self.text_world_in_file.place(x=730, y=90)
        self.word = tk.StringVar()
        self.word_in_file = tk.Entry(self.master, textvariable=self.word, width=20)
        self.word_in_file.place(x=730, y=110)

    def hidden_widgets(self):
        """
        UI configuration
        """
        self.create_date.destroy()
        self.modify_date.destroy()
        self.the_last_date.destroy()
        self.radio_one.destroy()
        self.radio_two.destroy()
        self.radio_three.destroy()
        self.text_size.destroy()
        self.text_world_in_file.destroy()
        self.word_in_file.destroy()

    def hidden_creation_calendar(self):
        """
        UI configuration
        """
        self.text_start_date.destroy()
        self.text_end_date.destroy()
        self.creation_cal_start.destroy()
        self.creation_cal_end.destroy()

    def hidden_modification_calendar(self):
        """
        UI configuration
        """
        self.text_start_date_modify.destroy()
        self.text_end_date_modify.destroy()
        self.modification_cal_start.destroy()
        self.modification_cal_end.destroy()

    def hidden_last_calendar(self):
        """
        UI configuration
        """
        self.text_start_date_last.destroy()
        self.text_end_date_last.destroy()
        self.last_cal_start.destroy()
        self.last_cal_end.destroy()

    def hidden_with_checkbox(self):
        """
        UI configuration
        """
        if self.hidden:
            self.select_creation_date_button()
            self.select_modification_date_button()
            self.select_last_date_button()
            self.hidden_size_radiobutton()
            self.hidden_word_in_file()
        else:
            self.hidden_widgets()
            if not self.creation_date:
                self.hidden_creation_calendar()
            if not self.modification_date:
                self.hidden_modification_calendar()
            if not self.last_date:
                self.hidden_last_calendar()
            self.creation_date = True
            self.modification_date = True
            self.last_date = True
        self.hidden = not self.hidden

    def enable_creation_date(self):
        """
        UI configuration
        """
        if self.creation_date:
            self.hidden_labels()
            self.hidden_creation_date()
        else:
            self.hidden_creation_calendar()
        self.creation_date = not self.creation_date

    def enable_modification_date(self):
        """
        UI configuration
        """
        if self.modification_date:
            self.hidden_modification_date()
            self.hidden_labels_modification_date()
        else:
            self.hidden_modification_calendar()
        self.modification_date = not self.modification_date

    def enable_last_date(self):
        """
        UI configuration
        """
        if self.last_date:
            self.hidden_last_date()
            self.hidden_labels_last_date()
        else:
            self.hidden_last_calendar()
        self.last_date = not self.last_date

    def select_path_from_button(self):
        """
        UI configuration
        """
        self.filename = filedialog.askdirectory()
        self.path_str.set(self.filename)

    def exit_application(self):
        """
        UI configuration
        """
        self.master.destroy()

    def result_of_search(self):
        """
        UI configuration
        """
        self.list_of_result = ttk.Treeview(self.master, height=24, columns=("size",
                                                                            "type",
                                                                            "creation date",
                                                                            "last modification date",
                                                                            "last access date",
                                                                            "owner"))
        self.list_of_result.heading("#0", text="Archive")
        self.list_of_result.heading("size", text="Size")
        self.list_of_result.heading("type", text="Type")
        self.list_of_result.heading("creation date", text="Creation Date")
        self.list_of_result.heading("last modification date", text="Modification Date")
        self.list_of_result.heading("last access date", text="Last access Date")
        self.list_of_result.heading("owner", text="Owner")
        self.list_of_result.place(x=10, y=180)

    def valid_date_message_error(self):
        """
        UI configuration
        """
        messagebox.showerror("Error", "The end final date is before initial date or invalid date format")

    def search_criteria(self):
        """
        UI configuration
        """
        get_path = self.path_str.get()
        get_key = self.key_str.get()
        self._search_criteria.set_search_filter({"path": get_path})
        self._search_criteria.set_search_filter({"file_name": get_key})
        if not self.hidden:
            self._search_criteria.set_search_filter({"advance_flag": True})
            if not self.creation_date:
                get_creation_start_date = self.create_date_value.get()
                get_creation_end_date = self.create_date_end_value.get()
                valid_date = utils.are_date_valid(get_creation_start_date, get_creation_end_date)
                if valid_date:
                    self._search_criteria.set_search_filter({"creation_date": {"start_date": get_creation_start_date,
                                                                               "end_date": get_creation_end_date}})
                else:
                    self.valid_date_message_error()
                    self.error = False
            if not self.modification_date:
                get_modification_start_date = self.modification_date_value.get()
                get_modification_end_date = self.modification_date_end_value.get()
                self._search_criteria.set_search_filter({"modification_date": {
                    "start_date": get_modification_start_date,
                    "end_date": get_modification_end_date}})
            if not self.last_date:
                get_last_start_date = self.last_date_value.get()
                get_last_end_date = self.last_date_end_value.get()
                self._search_criteria.set_search_filter({"last_access_date": {"start_date": get_last_start_date,
                                                                              "end_date": get_last_end_date}})
        list_d = self.search_obj.create_list_of_ocurrences(self._search_criteria)
        if not self.error:
            self.list_of_result.insert("", tk.END, text="No results found", values="")
        else:
            if list_d:
                for value in list_d:
                    self.list_of_result.insert("", tk.END, text=value.get_file_name(),
                                               values=(str(int(value.get_file_size()) / 1000000),
                                               value.get_file_type(),
                                               time.asctime(time.localtime(value.get_creation_time())),
                                               time.asctime(time.localtime(value.get_last_modification_date())),
                                               time.asctime(time.localtime(value.get_last_modification_date())), ""))
            else:
                self.list_of_result.insert("", tk.END, text="No results found", values="")


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
    main()