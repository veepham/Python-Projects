# File Transfer Assignment
#
# Version: Python 3.11.0
#
# Prompt:   Creating a program that move files from one folder to another
#           with a click of a button. Write a script that creates a GUI.
#           
#           
#

import tkinter as tk
from tkinter import *
import tkinter.filedialog

import os
import time
import shutil

from datetime import datetime, timedelta

# Set up GUI window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # Sets title of GUI window
        self.master.title('File Transfer')

        # Create buttons and entry text boxes
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,0))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,0))

        # button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        # exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    # Function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0,END) # clears the content inserted into entry field
        self.source_dir.insert(0, selectSourceDir)

    # Function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)

    # Function to transfer files from one directory to another
    def transferFiles(self):
        source = self.source_dir.get() # gets source directory
        destination = self.destination_dir.get() # gets destination directory
        Yesterday = datetime.now() + timedelta(hours=-24)
        
        source_files = os.listdir(source) # gets list of files in the source directory
        f = 0
        while f < len(source_files): # runs through each file in source directory
            filePath = os.path.join(source, source_files[f])
            mtime = os.path.getmtime(filePath)
            local_time = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
            if local_time > str(Yesterday):
                shutil.move(source + '/' + source_files[f], destination)
                print(source_files[f] + ' was successfully transferred.')
            else:
                print(source_files[f] + ' is not under 24 hours old.')
            f = f + 1
        

    def exit_program(self):
        root.destroy()

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
