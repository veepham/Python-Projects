import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False) # False means text box will not be resizable
        self.master.geometry('{}x{}'.format(700,400)) # Setting a default size for window
        self.master.title('Learning Tkinter') # Window title
        self.master.config(bg='lightgray') # background color, can also use hex code

        self.varFName = StringVar() # defining variables, remember to use self to connect back to class
        self.varLName = StringVar()


        self.lblFName = Label(self.master, text='First Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0,column=0,padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master, text='Last Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1,column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0), pady=(30,0))
       

        # creating a text box (entry), self.master refers to where we want the box (master is the main window)
        self.txtFName = Entry(self.master, text=self.varFName, font=('Helvetica', 16), fg='black', bg='lightblue')
        # grid is the command to paint what we wrote in the last line into the window (look up grid vs pack)
        self.txtFName.grid(row=0,column=1,padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master, text=self.varLName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1,column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello, {} {}!'.format(fn,ln))
        

    def cancel(self):
        self.master.destroy()
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
