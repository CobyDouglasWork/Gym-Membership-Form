from tkinter import *
import tkinter.messagebox
import tkinter.font as TkFont
import booking
import Register
import main_menu
import Search_form
import os
import sqlite3
from sqlite3 import Error

class Help:
    #Response to button function
    def form_response_fn(self,choice):
        win = Toplevel()

        if (choice==1):
            form_next = Search_form.Search_form(win)
        elif (choice==2):
            form_next = Register.Register(win)
        elif (choice==3):
            form_next = booking.booking(win)
        # elif (choice==4):
        #     form_next = Help.Help(win)
        elif (choice==5):
            form_next = main_menu.main_menu(win)
        else:
            self.window.destroy()
        
        self.window.withdraw()
        win.deiconify

    def __init__(self, window):
        #get field values
        get_info = 1

        #Building the form
        self.window = window
        self.window.title("Gym Membership Form")
        self.window.geometry("500x750")
        self.window.resizable(0,0)
        title_font = TkFont.Font(size=18,weight="bold")
        heading = Label(self.window, text = "Help", bg = "grey", fg = "black", width = "500", height = "1", font = title_font)
        heading_font = TkFont.Font(size=12,weight="bold",underline=True)
        heading.pack()

        #Help
        #main menu
        main_menu_heading = Label(self.window, text = "Main menu",font = heading_font)
        main_menu_heading.place(x = 170, y = 50)

        main_menu_text = Label(self.window, text = "The main menu is the start of the gym application and allows you to see ""\n""the functions of the gym app.")
        main_menu_text.place(x = 50, y = 80)
        #Registration
        registration_heading = Label(self.window, text = "Registration",font = heading_font)
        registration_heading.place(x = 170, y = 130)

        registration_text = Label(self.window, text = "The registration form is to add new members to the gym ""\n"" database so that people can sign up.")
        registration_text.place(x = 50, y = 160)

        #Booking form
        booking_class_heading = Label(self.window, text = "Booking class",font = heading_font)
        booking_class_heading.place(x = 170, y = 210)

        booking_text = Label(self.window, text = " The booking form is to book the members of the gym into""\n"" different classes and store what classes each person is taking.")
        booking_text.place(x = 50, y = 240)
        #Search form
        search_form_heading = Label(self.window, text = "Search form",font = heading_font)
        search_form_heading.place(x = 170, y = 290)

        search_form_text = Label(self.window, text = "The search from is to see the members of the gyms data.""\n"" this could help as we can see data on how to imporve the company ""\n""by seeing what kind of things the gym members like and dont like.")
        search_form_text.place(x = 50, y = 320)

        #exit
        exit_heading = Label(self.window, text = "Exit",font = heading_font)
        exit_heading.place(x = 170, y = 380)

        exit_text = Label(self.window, text = "The exit button is to close the gym application.")
        exit_text.place(x = 50, y = 410)

        #Other options
        search_form = Button(self.window,text = "Search form", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(1))
        regristration = Button(self.window,text = "Regristration", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(2))
        booking_class = Button(self.window,text = "Booking class", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(3))
        main_menu = Button(self.window,text = "Main menu", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(5))
        exit = Button(self.window,text = "Exit", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(6))
        
        search_form.place(x = 90, y = 650)
        regristration.place(x = 90, y = 550)
        booking_class.place(x = 90, y = 600)
        main_menu.place(x = 90, y = 500)
        exit.place(x = 90, y = 700)

def page():
    window = Tk()
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()