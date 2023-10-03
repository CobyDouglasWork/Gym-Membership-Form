from tkinter import *
import tkinter.messagebox
import tkinter.font as TkFont
import booking
import Help
import main_menu
import Search_form
import os
import sqlite3
from sqlite3 import Error
 
# -----  connect to the SQLite database -----
#    create it if it does not exist
def dbconnect():
    conn = None
    try:
        conn = sqlite3.connect(os.getcwd() + "/Gym_Database.db" )
    except Error as e:
        print(e)
        return None
    return conn


class Register:
    #Response to button function
    def form_response_fn(self,choice):
        win = Toplevel()
        
        if (choice==1):
            form_next = Search_form.Search_form(win)
        # elif (choice==2):
        #     form_next = Register.Register(win)
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
        firstname_info = self.firstname.get()
        if firstname_info == "":
            error_message = "please fill in firstname field"
        elif firstname_info.isalpha() == False:
            error_message = "no numbers or special characters in the fistname field"

        lastname_info = self.lastname.get()
        if lastname_info == "":
            error_message = "please fill in lastname field"
        elif lastname_info.isalpha() == False:
            error_message = "no numbers or special characters in the lastname field"

        address_info = self.address.get()
        if address_info == "":
            error_message = "please fill in address field"

        mobile_number_info = self.mobile_number.get()
        if mobile_number_info == "":
            error_message = "please fill in the mobile number field" 
        elif mobile_number_info.isdigit() == False:
            error_message = "Only numbers in the mobile number field"

        access_extra_cost = 0
        if self.access.get() == "1":
            access_extra_cost += 1
            extras += "24/7, "
        elif self.access.get() == "0":
            access_extra_cost = 0
        else:
            error_message = "please select an option for access 24 hour"

        trainer_extra_cost = 0
        if self.personal_trainer.get() == "1":
            trainer_extra_cost += 20
            extras += "trainer, "
        elif self.personal_trainer.get() == "0":
            trainer_extra_cost = 0
        else:
            error_message = "please select an option for personal trainer"

        diet_extra_cost = 0
        if self.diet_consult.get() == "1":
            diet_extra_cost += 20
            extras += "diet, "
        elif self.diet_consult.get() == "0":
            diet_extra_cost = 0
        else:
            error_message = "please select an option for a diet consultant"

        videos_extra_cost = 0
        if self.videos.get() == "1":
            videos_extra_cost += 2
            extras += "videos, "
        elif self.videos.get() == "0":
            videos_extra_cost = 0
        else:
            error_message = "please select an option for online videos"

        frequency_of_payment_info = None
        weeks = 0
        if self.frequency.get() == "1":
            frequency_of_payment_info = "weekley"
            weeks = 1
        elif self.frequency.get() == "0":
            frequency_of_payment_info = "Monthly"
            weeks = 4
        else:
            error_message = "please select an option for Frequency of Payement"

        memberhip_type_info = None
        membership_type_id = 1
        base_membership_cost = 0
        if self.memberhip_type.get() == "Basic ($10 per week)":
            base_membership_cost += 10
            memberhip_type_info = "Basic"
        elif self.memberhip_type.get() == "Regular ($15 per week)":
            base_membership_cost += 15
            memberhip_type_info = "Regular"
            membership_type_id = 2
        elif self.memberhip_type.get() == "Premium ($20 per week)":
            base_membership_cost += 20
            memberhip_type_info = "Premium"
            membership_type_id = 3
        else:
            error_message = "please select an option for Type of Memebership"

        weekly_discount = 0
        if self.duration.get() == "3 months":
            weekly_discount = 0
        elif self.duration.get() == "12 months":
            weekly_discount = 2
        elif self.duration.get() == "24 months":
            weekly_discount = 5
        else:
            error_message = "please select an option for Duration"

        directdebit_discount = 1
        method_of_payment_info = "Credit"
        if self.directdebit.get() == "1":
            directdebit_discount = 0.99
            method_of_payment_info = "Direct Debit"
        elif self.directdebit.get() == "None":
            error_message = "please select an option for Direct Debit"


        if error_message == "":
            #.txt files variable calculations
            extra_cost = access_extra_cost + trainer_extra_cost + diet_extra_cost + videos_extra_cost

            total_discount = weekly_discount + (base_membership_cost * (1 - directdebit_discount))

            net_cost = base_membership_cost + extra_cost - total_discount
            
            regular_payment_info = net_cost * weeks

            insertsql = "insert into members (FirstName, LastName, Address, MobileNumber, PaymentFrequency, Extras, MembershipID, RegularPayment) "
            insertsql += "values ('"+  firstname_info + "','" + lastname_info + "','" + address_info + "','" + mobile_number_info + "'," + str(weeks) + ",'" + extras + "'," + str(membership_type_id) + "," + str(regular_payment_info) + ")"
            
            cur = conn.cursor()
            cur.execute(insertsql)
            conn.commit()


        else:
            #display error msg in pop up msgbox
            tkinter.messagebox.showinfo(title="Error", message = error_message)


    def __init__(self, window):
        #Building the form
        self.window = window
        self.window.title("Gym Membership Form")
        self.window.geometry("500x1000")
        self.window.resizable(0,0)
        self.title_font = TkFont.Font(size=18,weight="bold")
        self.heading = Label(self.window, text = "Gym Membership Form", bg = "grey", fg = "black", width = "500", height = "1", font = self.title_font)
        self.heading_font = TkFont.Font(size=12,weight="bold",underline=True)
        self.heading.pack()

        column_one_x = 50
        column_two_x = 165
        column_three_x = 245
        column_four_x = 295
        column_five_x = 335
        column_six_x = 365

        # Customer Details

        self.window.customer_heading = Label(self.window, text = "Customer Details", font = self.heading_font)
        firstname_text = Label(self.window, text = "Firstname:")
        lastname_text = Label(self.window, text = "Lastname:")
        address_text = Label(self.window, text = "Address:")
        mobile_number_text = Label(self.window, text = "Mobile Number:")

        self.window.customer_heading.place(x = 178, y = 50)
        firstname_text.place(x = column_one_x, y = 90)
        lastname_text.place(x = column_one_x, y = 120)
        address_text.place(x = column_one_x, y = 150)
        mobile_number_text.place(x = column_one_x, y = 180)

        self.firstname = StringVar()
        self.lastname = StringVar()
        self.address = StringVar()
        self.mobile_number = StringVar()

        firstname_entry = Entry(self.window, textvariable = self.firstname, width = "30")
        lastname_entry = Entry(self.window, textvariable = self.lastname, width = "30")
        addresss_entry = Entry(self.window, textvariable = self.address, width = "30")
        mobile_number_entry = Entry(self.window, textvariable = self.mobile_number, width = "30")

        firstname_entry.place(x = column_two_x, y = 90)
        lastname_entry.place(x = column_two_x, y = 120)
        addresss_entry.place(x = column_two_x, y = 150)
        mobile_number_entry.place(x = column_two_x, y = 180)

        # Membership Details
        membership_heading = Label(self.window, text = "Membership Details",font = self.heading_font)
        memberhip_type_text = Label(self.window, text = "Membership Type:")
        duration_text = Label(self.window, text = "Duration:")
        message_font = TkFont.Font(size=8,slant="italic")
        message_1_text = Label(self.window, text = "Sign up for a 12-month contract to recieve a $2 per week discount.", font = message_font)
        message_2_text = Label(self.window, text = "Sign up for 24 months to receive a $5 per week discount on any membership type.", font = message_font)

        membership_heading.place(x = 170, y = 220)
        memberhip_type_text.place(x = column_one_x, y = 260)
        duration_text.place(x = column_one_x, y = 290)
        message_1_text.place(x = column_one_x, y = 320)
        message_2_text.place(x = column_one_x, y = 350)

        self.memberhip_type = StringVar(self.window)
        self.memberhip_type.set("Select") # default value

        memberhip_type_box = OptionMenu(self.window, self.memberhip_type, "Basic ($10 per week)", "Regular ($15 per week)", "Premium ($20 per week)")
        memberhip_type_box.pack()
        memberhip_type_box.place(x = column_two_x, y = 260)

        self.duration = StringVar(self.window)
        self.duration.set("Select") # default value

        duration_box = OptionMenu(self.window, self.duration, "3 months", "12 months", "24 months")
        duration_box.pack()
        duration_box.place(x = column_two_x, y = 290)

        # Payment Option
        payment_heading = Label(self.window, text = "Payment Option", font = self.heading_font)
        directdebit_text = Label(self.window, text = "Direct Debit:")
        message_3_text = Label(self.window, text = "for direct debits, there is a 1% discount on the base membership cost.", font = message_font)
        frequency_text = Label(self.window, text = "Frequency Of Payment:")

        payment_heading.place(x = 180, y = 380)
        directdebit_text.place(x = column_one_x, y = 420)
        message_3_text.place(x = column_one_x, y = 450)
        frequency_text.place(x = column_one_x, y = 480)

        self.directdebit = StringVar()
        self.directdebit.set(None)
        rb1 = Radiobutton(self.window,text = "Yes",value=True,variable=self.directdebit)
        rb2 = Radiobutton(self.window,text = "No",value=False,variable=self.directdebit)

        self.frequency = StringVar()
        self.frequency.set(None)
        rb3 = Radiobutton(self.window,text = "Weekly",value = TRUE,variable=self.frequency)
        rb4 = Radiobutton(self.window,text = "Monthly",value=False,variable=self.frequency)

        rb1.place(x = column_three_x, y = 420)
        rb2.place(x = column_five_x, y = 420)
        rb3.place(x = column_three_x, y = 480)
        rb4.place(x = column_five_x, y = 480)

        # Extras
        extra_heading = Label(self.window, text = "Extras",font = self.heading_font)
        access_text = Label(self.window, text = "24/7 Access ($1 per week):")
        trainer_text = Label(self.window, text = "Personal Trainer ($20 per week):")
        diet_text = Label(self.window, text = "Diet Consultation ($20 per week):")
        videos_text = Label(self.window, text = "Access Online Fitness Videos ($2 per week):")

        extra_heading.place(x = 215, y = 520)
        access_text.place(x = column_one_x, y = 550)
        trainer_text.place(x = column_one_x, y = 580)
        diet_text.place(x = column_one_x, y = 610)
        videos_text.place(x = column_one_x, y =640)

        self.access = StringVar()
        self.access.set(None)
        rb1_extra = Radiobutton(self.window,text = "Yes",value = TRUE,variable=self.access)
        rb2_extra = Radiobutton(self.window,text = "No",value = FALSE,variable=self.access)

        self.personal_trainer = StringVar()
        self.personal_trainer.set(None)
        rb3_extra = Radiobutton(self.window,text = "Yes",value = TRUE,variable=self.personal_trainer)
        rb4_extra = Radiobutton(self.window,text = "No",value = FALSE,variable=self.personal_trainer)

        self.diet_consult = StringVar()
        self.diet_consult.set(None)
        rb5_extra = Radiobutton(self.window,text = "Yes",value = TRUE,variable=self.diet_consult)
        rb6_extra = Radiobutton(self.window,text = "No",value = FALSE,variable=self.diet_consult)

        self.videos = StringVar()
        self.videos.set(None)
        rb7_extra = Radiobutton(self.window,text = "Yes",value = TRUE,variable=self.videos)
        rb8_extra = Radiobutton(self.window,text = "No",value = FALSE,variable=self.videos)

        rb1_extra.place(x = column_four_x, y = 550)
        rb2_extra.place(x = column_six_x, y = 550)
        rb3_extra.place(x = column_four_x, y = 580)
        rb4_extra.place(x = column_six_x, y = 580)
        rb5_extra.place(x = column_four_x, y = 610)
        rb6_extra.place(x = column_six_x, y = 610)
        rb7_extra.place(x = column_four_x, y = 640)
        rb8_extra.place(x = column_six_x, y = 640)

        #button
        submit = Button(self.window,text = "Submit", font=14, fg='white', width = "34", height = "1", command = self.save_info, bg = "grey")
        submit.place(x = 90, y = 700)

        #window.mainloop()

        search_form = Button(self.window,text = "Search form", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(1))
        booking_class = Button(self.window,text = "Booking class", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(3))
        help = Button(self.window,text = "Help", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(4))
        main_menu = Button(self.window,text = "Main menu", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(5))
        exit = Button(self.window,text = "Exit", font=14, fg='white', width = "34", height = "1", bg = "grey", command=lambda:self.form_response_fn(6))
    
        search_form.place(x = 90, y = 760)
        booking_class.place(x = 90, y = 800)
        help.place(x = 90, y = 840)
        main_menu.place(x = 90, y = 880)
        exit.place(x = 90, y = 920)

def page():
    window = Tk()
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    page()