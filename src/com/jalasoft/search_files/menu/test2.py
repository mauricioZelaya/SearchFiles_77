from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter import ttk
import sys

import time

from src.com.jalasoft.search_files.utils import utils as utils
from src.com.jalasoft.search_files.search.search_engine import Search
from src.com.jalasoft.search_files.search.search_criteria import SearchCriteria
#
#
# class Application(ttk.Frame):
#
#     def __init__(self, main_window):
#         super().__init__(main_window)
#         main_window.title("Posicionar elementos en Tcl/Tk")
#
#         main_window.configure(width=300, height=200)
#         # Ignorar esto por el momento.
#         self.place(relwidth=1, relheight=1)
#         self.button = ttk.Button(self, text="Hola, mundo!")
#         self.button.place(x=20, y=40)
#
# def main_run():
#     main_window = tk.Tk()
#     app = Application(main_window)
#     app.mainloop()
#
#
# if __name__ == '__main__':
#     main_run()

# from tkinter import ttk
import tkinter as tk
# from popup import RightClickMenu


# class MyTestApp(tk.Frame):
#    def __init__(self, parent):
#        self.master = parent
#        tk.Frame.__init__(self, self.master)
#        self.configure_gui()
#        self.create_widgets()
#        # self.bind_right_click_menu_to_typing_area()
#
#    def configure_gui(self):
#        self.master.title('MY Test App')
#
#    def create_widgets(self):
#        self.create_text_area()
#        self.create_exit_button()
#
#    def create_text_area(self):
#        self.text_area = tk.Text(self.master, borderwidth=2, relief='sunken')
#        self.text_area.config(height=30, width=80)
#        self.text_area.grid(row=0, column=0, sticky="new")
#
#    def create_exit_button(self):
#        self.exit_btn = ttk.Button(self.master, text='Exit', command=self.exit_application)
#        self.exit_btn.grid(row=1, column=0, sticky='W', pady=15)
#
#    # def bind_right_click_menu_to_typing_area(self):
#    #     self.popup = RightClickMenu(self.master, self.text_area)
#    #     self.text_area.bind("<Button-3>", self.popup.popup_text)
#
#    def exit_application(self):
#        self.master.destroy()
#
# def main():
#    root = tk.Tk()
#    MyTestApp(root)
#    root.mainloop()
#
# if __name__ == '__main__':
#    main()

from tkinter import Tk, Checkbutton, DISABLED
# root = Tk()
# def click():
#     check.config(state=DISABLED)
# check = Checkbutton(text="Click Me", command=click)
# check.grid()
# root.mainloop()

# def toggle_entry():
#     global hidden
#     print(hidden)
#     if hidden:
#         e.grid()
#     else:
#         e.grid_remove()
#     hidden = not hidden
#
# hidden = False
# root = tk.Tk()
# e = tk.Entry(root)
# e.grid(row=0, column=1)
# tk.Button(root, text='Toggle entry', command=toggle_entry).grid(row=0, column=0)
# root.mainloop()

# try:
#     import tkinter as tk
#     from tkinter import ttk
# except ImportError:
#     import Tkinter as tk
#     import ttk
#
# from tkcalendar import Calendar, DateEntry
#
# def example1():
#     def print_sel():
#         print(cal.selection_get())
#
#     top = tk.Toplevel(root)
#
#     cal = Calendar(top,
#                    font="Arial 14", selectmode='day',
#                    cursor="hand1", year=2018, month=2, day=5)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()
#
# def example2():
#     top = tk.Toplevel(root)
#
#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
#
#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2)
#     cal.pack(padx=10, pady=10)
#
# root = tk.Tk()
# s = ttk.Style(root)
# s.theme_use('clam')
#
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)
#
# root.mainloop()

from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
