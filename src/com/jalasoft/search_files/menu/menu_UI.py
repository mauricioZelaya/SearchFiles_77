"""
Menu UI
"""

from tkinter import ttk
import tkinter as tk
import time
from tkcalendar import Calendar, DateEntry

from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria


class SearchMenu(tk.Frame):
    """
    Start menu
    """
    def __init__(self, parent, hidden, creation_date, modification_date, last_date, a):
        """
        Start menu
        """
        self.master = parent
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.last_date = last_date
        self.a = a
        self.hidden = hidden
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        """
        UI configuration
        """
        self.master.title('Menu Search')
        self.master.configure(width=800, height=800)
        # self.place(relwidth=1, relheight=1)

    def create_widgets(self):
        """
        Display all UI
        """
        self.create_labels()
        self.create_textbox()
        self.create_buttons()
        self.create_checkbox()

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
        self.path_entry = tk.Entry(self.master, textvariable=self.path_str, width=30)
        self.path_entry.place(x=90, y=40)
        self.key_str = tk.StringVar()
        self.key_entry = tk.Entry(self.master, textvariable=self.key_str, width=30)
        self.key_entry.place(x=90, y=75)

    def create_buttons(self):
        """
        all buttons
        """
        self.search = tk.Button(self.master, text="Search", command=None)
        self.search.place(x=200, y=100)
        self.cancel = tk.Button(self.master, text="Cancel", command=self.exit_application)
        self.cancel.place(x=270, y=100)
        self.path = tk.Button(self.master, text="Select Path", command=None)
        self.path.place(x=350, y=40)

    def create_checkbox(self):
        """
        all buttons
        """
        self.advanced = tk.Checkbutton(self.master, text="Advance", variable=None, onvalue=True,
                                       command=self.hidden_with_checkbox)
        self.advanced.place(x=350, y=100)

    def select_creation_date_button(self):
        """
        all Labels
        """
        self.create_date = tk.Button(self.master, text=".", command=self.enable_creation_date)
        self.create_date.place(x=470, y=120)

    def select_modification_date_button(self):
        """
        all Labels
        """
        self.modify_date = tk.Button(self.master, text=".", command=self.enable_modification_date)
        self.modify_date.place(x=470, y=180)

    def select_last_date_button(self):
        """
        all Labels
        """
        self.the_last_date = tk.Button(self.master, text=".", command=self.enable_last_date)
        self.the_last_date.place(x=470, y=240)


    def hidden_labels(self):
        """
        all Labels
        """
        self.text_c_day = tk.Label(self.master, text="Creation day :")
        self.text_c_day.place(x=350, y=130)
        self.text_m_day = tk.Label(self.master, text="Modification day :")
        self.text_m_day.place(x=350, y=190)
        self.text_l_day = tk.Label(self.master, text="Last Access day :")
        self.text_l_day.place(x=350, y=250)

    def hidden_creation_date(self):
        """
        all Labels
        """
        self.creation_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                            borderwidth=2)
        self.creation_cal_start.place(x=350, y=155)
        self.creation_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                          borderwidth=2)
        self.creation_cal_end.place(x=480, y=155)

    def hidden_modification_date(self):
        """
        all Labels
        """
        self.modification_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                            borderwidth=2)
        self.modification_cal_start.place(x=350, y=215)
        self.modification_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                          borderwidth=2)
        self.modification_cal_end.place(x=480, y=215)

    def hidden_last_date(self):
        """
        all Labels
        """
        self.last_cal_start = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                                borderwidth=2)
        self.last_cal_start.place(x=350, y=272)
        self.last_cal_end = DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                              borderwidth=2)
        self.last_cal_end.place(x=480, y=272)

    def hidden_size_radiobutton(self):
        """
        all Labels
        """
        self.var = tk.IntVar()
        self.radio_one = tk.Radiobutton(self.master, text="0 to 10 Mb", variable=self.var, value=1, command=None)
        self.radio_one.place(x=350, y=300)
        self.radio_two = tk.Radiobutton(self.master, text="11 to 100 Mb", variable=self.var, value=2, command=None)
        self.radio_two.place(x=350, y=320)
        self.radio_three = tk.Radiobutton(self.master, text="Greater than 101 Mb", variable=self.var, value=3,
                                          command=None)
        self.radio_three.place(x=350, y=340)

    def hidden_widgets(self):
        """
        UI configuration
        """
        self.text_c_day.destroy()
        self.text_m_day.destroy()
        self.text_l_day.destroy()
        self.create_date.destroy()
        self.modify_date.destroy()
        self.the_last_date.destroy()
        self.radio_one.destroy()
        self.radio_two.destroy()
        self.radio_three.destroy()

    def hidden_creation_calendar(self):
        """
        UI configuration
        """
        self.creation_cal_start.destroy()
        self.creation_cal_end.destroy()

    def hidden_modification_calendar(self):
        """
        UI configuration
        """
        self.modification_cal_start.destroy()
        self.modification_cal_end.destroy()

    def hidden_last_calendar(self):
        """
        UI configuration
        """
        self.last_cal_start.destroy()
        self.last_cal_end.destroy()

    def hidden_with_checkbox(self):
        """
        UI configuration
        """
        if self.hidden:
            self.hidden_labels()
            self.select_creation_date_button()
            self.select_modification_date_button()
            self.select_last_date_button()
            self.hidden_size_radiobutton()
        else:
            self.hidden_widgets()
        self.hidden = not self.hidden

    def enable_creation_date(self):
        """
        UI configuration
        """
        if self.creation_date:
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
        else:
            self.hidden_modification_calendar()
        self.modification_date = not self.modification_date

    def enable_last_date(self):
        """
        UI configuration
        """
        if self.last_date:
            self.hidden_last_date()
        else:
            self.hidden_last_calendar()
        self.last_date = not self.last_date

    def exit_application(self):
        """
        UI configuration
        """
        self.master.destroy()


def main():
    hidden = True
    modification_date = True
    creation_date = True
    last_date = True
    radio = True
    root = tk.Tk()
    SearchMenu(root, hidden, modification_date, creation_date, last_date, radio)
    root.mainloop()


if __name__ == '__main__':
    main()