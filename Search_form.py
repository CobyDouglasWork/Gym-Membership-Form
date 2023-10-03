from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.messagebox
import tkinter.font as TkFont
import booking
import Help
import main_menu
import Register
import os
import sqlite3
from sqlite3 import Error


class Search_form:

    #Response to button function
    def form_response_fn(self,choice):
        # if (choice==1):
        #     form_next = Search_form.Search_form(win)
        # el
        win = Toplevel()

        if (choice==2):
            form_next = Register.Register(win)
        elif (choice==3):
            form_next = booking.booking(win)
        elif (choice==4):
            form_next = Help.Help(win)
        elif (choice==5):
            form_next = main_menu.main_menu(win)
        else:
            self.window.destroy()
       
        self.window.withdraw()
        win.deiconify

    def get_info(self):
        self.tree.delete(*self.tree.get_children())
        conn = None
        try:
            conn = sqlite3.connect(os.getcwd() + "/Gym_Database.db" )
        except Error as e:
            print(e)

        searchSql = ""
        if (self.lastname_search.get() != ""):
            searchSql = "Select MemberID, FirstName, LastName, Address, MobileNumber, PaymentFrequency, Extras, MembershipID, RegularPayment from members where Lastname like '%" + self.lastname_search.get() + "%'"

        if (self.memberID_search.get() != ""):
            searchSql = "Select MemberID, FirstName, LastName, Address, MobileNumber, PaymentFrequency, Extras, MembershipID, RegularPayment from members where MemberID = '" + self.memberID_search.get() + "'"

        if (self.memberhip_type_entry.get() != "Select"):
            searchSql = searchSql + " and MembershipID = "
            if (self.memberhip_type_entry.get() == "Basic ($10 per week)"):
                searchSql = searchSql + " 1"
            if (self.memberhip_type_entry.get() == "Regular ($15 per week)"):
                searchSql = searchSql + " 2"
            if (self.memberhip_type_entry.get() == "Premium ($20 per week)"):
                searchSql = searchSql + " 3"

        
        if (self.lastname_search.get() == "" and self.memberID_search.get() == "" and self.memberhip_type_entry.get() != "Select"):
            searchSql = "Select MemberID, FirstName, LastName, Address, MobileNumber, PaymentFrequency, Extras, MembershipID, RegularPayment from members where MemberShipID = " 
            if (self.memberhip_type_entry.get() == "Basic ($10 per week)"):
                searchSql = searchSql + " 1"
            if (self.memberhip_type_entry.get() == "Regular ($15 per week)"):
                searchSql = searchSql + " 2"
            if (self.memberhip_type_entry.get() == "Premium ($20 per week)"):
                searchSql = searchSql + " 3"

       
        cur = conn.cursor()
        cur.execute(searchSql)
        rows = cur.fetchall()
        for row in rows:
          self.memberID_text_result.set = row[6]
          data = []
          self.tree.insert('', tk.END, values=(f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[4]}', f'{row[5]}', f'{row[6]}', f'{row[7]}', f'{row[8]}'))

       

        cur.close()

    def __init__(self, window):
        #Building the form
        self.window = window
        self.window.title("Gym Membership Form")
        self.window.geometry("1000x750")
        self.window.resizable(0,0)
        title_font = TkFont.Font(size=18,weight="bold")
        heading = Label(self.window, text = "Search Form", bg = "grey", fg = "black", width = "500", height = "1", font = title_font)
        heading_font = TkFont.Font(size=12,weight="bold",underline=True)
        heading.grid(row=0, column=0, sticky='nsew')

        column_one_x = 50
        column_two_x = 480
        column_three_x = 245
        column_four_x = 295
        column_five_x = 335
        column_six_x = 365



        # Search form

        search_heading = Label(self.window, text = "Search by",font = heading_font)
        memberID_text = Label(self.window, text = "Member ID: ")
        lastname_search_text = Label(self.window, text = "Lastname: ")
        MemebershipType_search_text = Label(self.window, text = "Membership type: ")

        search_heading.place(x = 350, y = 260)
        memberID_text.place(x = 350, y = 290)
        lastname_search_text.place(x = 350, y = 320)
        MemebershipType_search_text.place(x = 350, y = 350)

        self.memberID_search = StringVar()
        self.lastname_search = StringVar()


        firstname_entry = Entry(self.window, textvariable = self.memberID_search, width = "30")
        lastname_entry = Entry(self.window, textvariable = self.lastname_search, width = "30")
        self.memberhip_type_entry = StringVar(self.window)
        self.memberhip_type_entry.set("Select") # default value

        memberhip_type_box = OptionMenu(self.window, self.memberhip_type_entry, "Select", "Basic ($10 per week)", "Regular ($15 per week)", "Premium ($20 per week)")
        memberhip_type_box.grid()

        firstname_entry.place(x = column_two_x, y = 290)
        lastname_entry.place(x = column_two_x, y = 320)
        memberhip_type_box.place(x = column_two_x, y = 350)

        self.memberID_text_result = Label(self.window, text = "")
        self.memberID_text_result.place(x = column_one_x, y = 420)
        #button
        error = ""
        search = Button(self.window, text = "Search", font=14, fg='white', width = "34", height = "1", command = self.get_info, bg = "grey")
        search.place(x = 350, y = 430)

        # define columns
        columns = ('MemberID', 'FirstName', 'LastName', 'Address', 'MobileNumber', 'PaymentFrequency', 'Extras', 'MembershipID', 'RegulaurPayment')

        self.tree = ttk.Treeview(self.window, columns=columns, show='headings')

        # define headings
        self.tree.heading('MemberID', text='MemberID')
        self.tree.column('MemberID', minwidth=0, width=100, stretch=NO)
        self.tree.heading('FirstName', text='First Name')
        self.tree.column('FirstName', minwidth=0, width=100, stretch=NO)
        self.tree.heading('LastName', text='Last Name')
        self.tree.column('LastName', minwidth=0, width=100, stretch=NO)
        self.tree.heading('Address', text='Address')
        self.tree.column('Address', minwidth=0, width=100, stretch=NO)
        self.tree.heading('MobileNumber', text='Mobile Number')
        self.tree.column('MobileNumber', minwidth=0, width=100, stretch=NO)
        self.tree.heading('PaymentFrequency', text='Payment Frequency')
        self.tree.column('PaymentFrequency', minwidth=0, width=100, stretch=NO)
        self.tree.heading('Extras', text='Extras')
        self.tree.column('Extras', minwidth=0, width=100, stretch=NO)
        self.tree.heading('MembershipID', text='Membership')
        self.tree.column('MembershipID', minwidth=0, width=100, stretch=NO)
        self.tree.heading('RegulaurPayment', text='Regulaur Payment')
        self.tree.column('RegulaurPayment', minwidth=0, width=100, stretch=NO)    

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                showinfo(title='Information', message=','.join(record))


        self.tree.bind('<<TreeviewSelect>>', item_selected)

        self.tree.grid(row=0, column=0, sticky='nsew')


       

        #Other options
        regristration = Button(self.window,text = "Regristration", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(2))
        booking_class = Button(self.window,text = "Booking class", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(3))
        help = Button(self.window,text = "Help", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(4))
        main_menu = Button(self.window,text = "Main menu", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(5))
        exit = Button(self.window,text = "Exit", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(6))
       
        regristration.place(x = 350, y = 550)
        booking_class.place(x = 350, y = 600)
        help.place(x = 350, y = 650)
        main_menu.place(x = 350, y = 500)
        exit.place(x = 350, y = 700)


def page():
    window = Tk()
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()