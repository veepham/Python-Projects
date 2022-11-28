#
# Python Ver:   3.11.0
#
# Author:       Vivian Pham - Tech Academy
#
# Purpose:      Student Tracking System modeled after phonebook project.
#               
#

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_gui
import student_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(600,400) #height,width of window
        self.master.maxsize(600,400)
        # center_window() centers app on user's screen
        student_func.center_window(self,600,400)
        self.master.title('Student Tracking Assignment')
        self.master.configure(bg='#F0F0F0')

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module to keep code comparmentalized
        student_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

