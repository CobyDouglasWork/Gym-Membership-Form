from tkinter import *
import tkinter.messagebox
import tkinter.font as TkFont
import Help
import booking
import Register
import Search_form
import os
import sqlite3
from sqlite3 import Error

class main_menu:

    #Response to button function
    def form_response_fn(self,choice):
        win = Toplevel()
        if (choice==1):
            form_next = Search_form.Search_form(win)
        elif (choice==2):
            form_next = Register.Register(win)
        elif (choice==3):
            form_next = booking.booking(win)
        elif (choice==4):
            form_next = Help.Help(win)
        # elif (choice==5):
        #     form_next = main_menu.main_menu(win)
        else:
            self.window.destroy()
        
    def __init__(self, window):
        #Building the form
        self.window = window
        self.window.title("Gym Membership Form")
        self.window.geometry("500x750")
        self.window.resizable(0,0)
        title_font = TkFont.Font(size=18,weight="bold")
        heading = Label(text = "Main Menu", bg = "grey", fg = "black", width = "500", height = "1", font = title_font)
        heading_font = TkFont.Font(size=12,weight="bold",underline=True)
        heading.pack()


        #Main menu
        search_form = Button(self.window,text = "Search form", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(1))
        regristration = Button(self.window,text = "Regristration", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(2))
        booking_class = Button(self.window,text = "Booking class", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(3))
        help = Button(self.window,text = "Help", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(4))
        exit = Button(self.window,text = "Exit", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(6))
        
        search_form.place(x = 90, y = 50)
        regristration.place(x = 90, y = 100)
        booking_class.place(x = 90, y = 150)
        help.place(x = 90, y = 200)
        exit.place(x = 90, y = 250)

    #Main loop
    # def run(self):
    #     self.root.mainloop()

def page():
    window = Tk()
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()