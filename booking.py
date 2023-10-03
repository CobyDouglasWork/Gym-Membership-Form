from tkinter import *
import tkinter.messagebox
import tkinter.font as TkFont
import Register
import Help
import main_menu
import Search_form
import os
import sqlite3
from sqlite3 import Error
from tkcalendar import Calendar
from datetime import datetime

class booking:
    #Response to button function
    def form_response_fn(self,choice):
        win = Toplevel()

        if (choice==1):
            form_next = Search_form.Search_form(win)
        elif (choice==2):
            form_next = Register.Register(win)
        # elif (choice==3):
        #     form_next = booking.booking(win)
        elif (choice==4):
            form_next = Help.Help(win)
        elif (choice==5):
            form_next = main_menu.main_menu(win)
        else:
            self.window.destroy()
       
        self.window.withdraw()
        win.deiconify

    #saves info from the form into a database
    def save_info(self) :
        #conn = dbconnect
        conn = None
        try:
            conn = sqlite3.connect(os.getcwd() + "/Gym_Database.db" )
        except Error as e:
            print(e)
         

        error_message = ""
        extras = ""
        #get field values

        cardio_info = FALSE
        weeks = 0
        if self.cardio.get() == "1":
            cardio_info = True
        elif self.cardio.get() == "0":
            cardio_info = FALSE
        else:
            error_message = "please select an option for  Cardio class"

        pilates_info = None
        weeks = 0
        if self.pilates.get() == "1":
            pilates_info = True
        elif self.pilates.get() == "0":
            pilates_info = FALSE
        else:
            error_message = "please select an option for Pilates class"

        spin_info = None
        weeks = 0
        if self.spin.get() == "1":
             spin_info = True
        elif self.spin.get() == "0":
            spin_info = FALSE
        else:
            error_message = "please select an option for Spin class"

        if error_message == "":
            cur = conn.cursor()
            if cardio_info:
                insertsql = "insert into Booking (MemberID, FitnessClassID) "
                insertsql += "select '"+  self.customer_ID.get() + "',1 where NOT EXISTS (select * from booking WHERE  MemberID = '"+  self.customer_ID.get() + "' AND fitnessClassID = 1)  "
                cur.execute(insertsql)
            else:
                deletesql = "delete from Booking where MemberID = '" + self.customer_ID.get() + "' and FitnessClassID = 1"
                cur.execute(deletesql)


            if pilates_info:
                insertsql = "insert into Booking (MemberID, FitnessClassID) "
                insertsql += "select '"+  self.customer_ID.get() + "',1 where NOT EXISTS (select * from booking WHERE  MemberID = '"+  self.customer_ID.get() + "' AND fitnessClassID = 1)  "
                cur.execute(insertsql)
            else:
                deletesql = "delete from Booking where MemberID = '" + self.customer_ID.get() + "' and FitnessClassID = 2"
                cur.execute(deletesql)

            if spin_info:
                insertsql = "insert into Booking (MemberID, FitnessClassID) "
                insertsql += "select '"+  self.customer_ID.get() + "',1 where NOT EXISTS (select * from booking WHERE  MemberID = '"+  self.customer_ID.get() + "' AND fitnessClassID = 1)  "
                cur.execute(insertsql)
            else:
                deletesql = "delete from Booking where MemberID = '" + self.customer_ID.get() + "' and FitnessClassID = 3"
                cur.execute(deletesql)



            conn.commit()


        else:
            #display error msg in pop up msgbox
            tkinter.messagebox.showinfo(title="Error", message = error_message)



    

    def get_info(self):
        self.pilates.set(None)
        self.spin.set(None)
        self.cardio.set(None)
        
        conn = None
        try:
            conn = sqlite3.connect(os.getcwd() + "/Gym_Database.db" )
        except Error as e:
            print(e)

        searchSql = ""
        if (self.customer_ID.get() != ""):
            searchSql = "Select FirstName, LastName, FitnessClass.ClassDescription from members left outer join booking on booking.MemberID = members.MemberID left outer join FitnessClass on FitnessClass.FitnessClassID = Booking.FitnessClassID where members.MemberID = " + self.customer_ID.get() + ""

        cur = conn.cursor()
        cur.execute(searchSql)
        rows = cur.fetchall()
        row_y = 220
        for row in rows:
          enrolled = Label(self.window, text = row)
          enrolled.place(x = 50, y = row_y)
          row_y = row_y + 20

          if "Pilates" in row[2]:
              self.pilates.set(True)
          if "Spin" in row[2]:
              self.spin.set(True)
          if "Cardio" in row[2]:
              self.cardio.set(True)


        cur.close()

    def __init__(self, window):
        #Building the form
        self.window = window
        self.window.title("Gym Membership Form")
        self.window.geometry("500x750")
        self.window.resizable(0,0)
        title_font = TkFont.Font(size=18,weight="bold")
        heading = Label(self.window, text = "Fitness booking class", bg = "grey", fg = "black", width = "500", height = "1", font = title_font)
        heading_font = TkFont.Font(size=12,weight="bold",underline=True)
        heading.pack()

        #Customer detail
        customer_heading = Label(self.window, text = "Customer details",font = heading_font)
        ID_heading = Label(self.window, text = "Customer ID number: ")

        customer_heading.place(x = 50, y = 50)
        ID_heading.place(x = 50, y = 80)

        self.customer_ID = StringVar()
       
        self.customer_ID_entry = Entry(self.window, textvariable = self.customer_ID, width = "30")
        self.customer_ID_entry.place(x = 200, y = 80)

        #ID button
        load = Button(self.window,text = "Load", font=14, fg='white', width = "34", height = "1", command = self.get_info, bg = "grey")
        load.place(x = 90, y = 120)

        #class date
        fitness_session_heading = Label(self.window, text = "Fitness session",font = heading_font)
        fitness_session_heading.place(x = 50, y = 160)

        #enrolled classes
        enrolled_heading = Label(self.window, text = "you are enrolled in:")
        enrolled_heading.place(x = 50, y = 190)

        #class type
        class_type_heading = Label(self.window, text = "Fitness class",font = heading_font)
        class_type_heading.place(x = 50, y = 330)
        self.window.class_ID = StringVar()

        cardio_text = Label(self.window, text = "Cardio, Thursday, 3 pm–5 pm")
        cardio_text.place(x = 50, y = 360)
        self.window.class_ID = StringVar()

        pilates_text = Label(self.window, text = "Pilates, Friday, 9 am–11 am")
        pilates_text.place(x = 50, y = 380)
        self.window.class_ID = StringVar()

        spin_text = Label(self.window, text = "Spin, Monday, 2 pm–4 pm")
        spin_text.place(x = 50, y = 400)
        self.window.class_ID = StringVar()

        book_text = Label(self.window, text = "book it  | dont book/unbook")
        book_text.place(x = 220, y = 330)

        self.cardio = StringVar()
        self.cardio.set(None)
        rb1 = Radiobutton(self.window,text = "",value = TRUE,variable=self.cardio)
        rb2 = Radiobutton(self.window,text = "",value = FALSE,variable=self.cardio)
       

        self.pilates = StringVar()
        self.pilates.set(None)
        rb3 = Radiobutton(self.window,text = "",value = TRUE,variable=self.pilates)
        rb4 = Radiobutton(self.window,text = "",value = FALSE,variable=self.pilates)

        self.spin = StringVar()
        self.spin.set(None)
        rb5 = Radiobutton(self.window,text = "",value = TRUE,variable=self.spin)
        rb6 = Radiobutton(self.window,text = "",value = FALSE,variable=self.spin)

        rb1.place(x = 220, y = 360)
        rb2.place(x = 280, y = 360)
        rb3.place(x = 220, y = 380)
        rb4.place(x = 280, y = 380)
        rb5.place(x = 220, y = 400)
        rb6.place(x = 280, y = 400)

        #submit button
        submit = Button(self.window,text = "Submit", font=14, fg='white', width = "34", height = "1", command = self.save_info, bg = "grey")
        submit.place(x = 90, y = 450)


        #Other options
        search_form = Button(self.window,text = "Search form", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(1))
        regristration = Button(self.window,text = "Regristration", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(2))
        help = Button(self.window,text = "Help", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(4))
        main_menu = Button(self.window,text = "Main menu", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(5))
        exit = Button(self.window,text = "Exit", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(6))
       
        search_form.place(x = 90, y = 650)
        regristration.place(x = 90, y = 550)
        help.place(x = 90, y = 600)
        main_menu.place(x = 90, y = 500)
        exit.place(x = 90, y = 700)

def page():
    window = Tk()
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()