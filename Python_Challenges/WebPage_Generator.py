# Web Page Generator Assignment
#
# Version: Python 3.11.0
#
# Prompt:   Create a tool that can automatically create a
#           basic HTML web page using Tkinter GUI.
#
#


import tkinter as tk
from tkinter import *

# webbrowser module allows creation of web documents
# and display them in the browser
import webbrowser 

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        self.varCText = StringVar() # defining variable

        # label for entry text box
        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl.grid(row=0,column=0, padx=(20,0), pady=(20,0))

        # entry field for custom text
        self.custText = Entry(self.master, text=self.varCText)
        self.custText.grid(row=1, column=0, columnspan=4, sticky=N+E+W, padx=(20,20), pady=(0,0))
        
        # button for generating web page
        self.Dbtn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.Dbtn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

        # button for generating custom page
        self.Cbtn = Button(self.master, text="Submit Custom Text", width=20, height=2, command=self.customHTML)
        self.Cbtn.grid(row=2, column=2, padx=(10,10), pady=(10,10))

        # button to cancel
        self.Closebtn = Button(self.master, text="Cancel", width=20, height=2, command=self.cancel)
        self.Closebtn.grid(row=2, column=3, padx=(10,10), pady=(10,10))
        

    # function for default button
    def defaultHTML(self):
        htmlText = "Stay tune for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # function for custom web page
    def customHTML(self):
        htmlText = self.varCText.get() # calling the entered text variable
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def cancel(self):
        self.master.destroy()
        
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
