
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def  main():
    root = Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("MvdB Software Solutions Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg ='khaki1')
        self.frame =Frame(self.master, bg ='khaki1')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        #title label
        self.lblTitle = Label (self.frame, text = 'MvdB Software Solutions Login System', font = 'arial 50 bold', bg = 'khaki1', fg = 'black')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 40)

        #login frames
        self.LoginFrame1 = LabelFrame(self.frame, width = 1350, height = 600
                                     ,font = 'arial 20 bold', relief = 'ridge', bg = 'IndianRed1', bd = 20)
        self.LoginFrame1.grid(row = 1, column = 0)

        self.LoginFrame2 = LabelFrame(self.frame, width = 1000, height = 600
                                     ,font = 'arial 20 bold', relief = 'ridge', bg = 'IndianRed1', bd = 20)
        self.LoginFrame2.grid(row = 2, column = 0)

        #text fields login&password
        self.lblUsername = Label(self.LoginFrame1, text = 'Username',font = 'arial 20 bold', bd = 22, bg = 'IndianRed1', fg = 'cornsilk')
        self.lblUsername.grid(row = 0, column = 0)
        self.txtUsername = Entry(self.LoginFrame1,font = 'arial 20 bold', textvariable = self.Username)
        self.txtUsername.grid(row = 0, column = 1)
        
        self.lblPassword = Label(self.LoginFrame1, text = 'Password',font = 'arial 20 bold', bd = 22, bg = 'IndianRed1', fg = 'cornsilk')
        self.lblPassword.grid(row = 1, column = 0)
        self.txtPassword = Entry(self.LoginFrame1,font = 'arial 20 bold', show = '*', textvariable = self.Password)
        self.txtPassword.grid(row = 1, column = 1)

        # creating buttons
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 20, font = 'arial 20 bold', command = self.Login_System)
        self.btnLogin.grid(row=3, column = 0, pady = 20 , padx = 8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 20, font = 'arial 20 bold', command = self.Reset)
        self.btnReset.grid(row=3, column = 1, pady = 20 , padx = 8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 20, font = 'arial 20 bold', command = self.Exit)
        self.btnExit.grid(row=3, column = 2, pady = 20 , padx = 8)

        #login info label
        self.lblTitle = Label (self.frame, text = 'To login use adam & 1234', font = 'arial 20', bg = 'khaki1', fg = 'black')
        self.lblTitle.grid(row = 4, column = 0, columnspan = 2, pady = 40)

    #loging btns logic
    #login btn
    def Login_System(self):
        u =(self.Username.get())
        p =(self.Password.get())
        if(u ==str('adam') and p ==str('1234')):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("MvdB Login System", "That's cute but it is WRONG! :((")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
            
    #reset btn
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    #exit btn
    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("MvdB Login System", "Really wanna exit?")
        if self.Exit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("MvdB Management System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg ='cadet blue')
        self.frame =Frame(self.master, bg ='cadet blue')
        self.frame.pack()

        #title label
        self.lblTitle = Label (self.frame, text = 'Loging successful. Welcome in restricted area :)', font = 'arial 30 bold', bg = 'cadet blue', fg = 'black')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 40)

#if __main__ == 'main':
main()
