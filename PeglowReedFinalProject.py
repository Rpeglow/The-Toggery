"""Author Reed Peglow
This program will take information from the customer of a small consignment store, it will validate that all required
 fields are filled and that the phone number is a 10-digit number. After successfully inputting all information, a
new window will display a contract that must be accepted to continue, if not accepted then the program will print the
user info with a disclaimer of "Canceled". After the user has agreed to the term and conditions of the contract,
a thank-you box will show confirming that their items have been accepted and are awaiting inspection by employee.
 The program will print and save the customers information for use by an employee."""
# import of tkinter and image processes
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

# variable for initializing the first window
root = tk.Tk()
root.geometry("650x650")
root.title("Welcome to the Toggery.")


# function to verify first and last name are inputted, also checking that the phone number includes area code.
def gather_info():
    # variable for name and phone
    firstname = e_first_name.get().title()
    lastname = e_last_name.get().title()
    phone = e_phone.get()

    if firstname and lastname:
        if len(phone) == 10 and phone.isdigit():
            terms_cond()
        else:
            tk.messagebox.showwarning(title="Error", message="Phone number must include area code.")

    else:
        tk.messagebox.showwarning(title="Error", message="First and Last name are required.")


# function to initialize the terms and conditions window that must be accepted to move forward or declined to cancel

def terms_cond():
    # variable for second image
    global my_image2
    # variable for second window
    window = Toplevel(root)
    window.geometry("1420x700")
    window.title("Terms and Conditions")
    window.state("zoomed")
    # variables for image labels and buttons
    my_image2 = ImageTk.PhotoImage(Image.open("terms.jpg"))
    my_label2 = Label(window, image=my_image2)
    my_label2.pack()
    btn_disagree = tk.Button(window, text='Cancel', command=cancel, font='Arial, 18')
    btn_disagree.place(x=850, y=650)
    btn_agree = tk.Button(window, text='Agree', command=agreed, font='Arial, 18')
    btn_agree.place(x=650, y=650)


# function to print and gather information and confirm that information was successfully accepted.
def agreed():
    # variable for finale image
    global my_img2
    # variable for user information
    firstname = e_first_name.get().title()
    lastname = e_last_name.get().title()
    phone = e_phone.get()
    address = txt_address.get('1.0', tk.END)
    # variable for last window
    processed = Toplevel(root)
    processed.title("Complete")
    # variables for labels and buttons
    my_img2 = ImageTk.PhotoImage(Image.open("toggery.JPG"))
    my_label2 = Label(processed, image=my_img)
    my_label2.pack()
    tk.Label(processed, text=f"Thank you {firstname} {lastname}").pack()
    tk.Label(processed, text=f"Your address is: {address}").pack()
    tk.Label(processed, text="Thank you for choosing The Toggery!").pack()
    tk.Label(processed, text=f"We will contact you at: {phone}, when we have finished processing your items.").pack()
    tk.Button(processed, text="Finished", command=finished).pack()
    # user_info variable would be used to add to existing database (note not functionally operational, yet!)
    user_info = (firstname, lastname, phone, address)


# function to gather information from a canceled transaction and to exit the program
def cancel():
    # variable for user information
    firstname = e_first_name.get().title()
    lastname = e_last_name.get().title()
    phone = e_phone.get()
    address = txt_address.get('1.0', tk.END)
    print("USER CANCELED")
    print("First Name:", firstname)
    print("Last Name:", lastname)
    print("Phone Number:", phone)
    print("Address:", address)
    print("USER CANCELED")
    exit()


# function to print and save user information and exit upon completion
def finished():
    # variable for user information
    firstname = e_first_name.get().title()
    lastname = e_last_name.get().title()
    phone = e_phone.get()
    address = txt_address.get('1.0', tk.END)
    print("First Name:", firstname)
    print("Last Name:", lastname)
    print("Phone Number:", phone)
    print("Address:", address)
    exit()


# the following code is for image use
my_img = ImageTk.PhotoImage(Image.open("toggery.JPG"))
my_label = Label(image=my_img)
my_label.pack()
# labels for first, last, phone, and address
label_f_name = tk.Label(root, text="Enter your First Name:", font=('Arial', 18))
label_f_name.pack()
e_first_name = Entry(root, width=50, borderwidth=3)
e_first_name.pack()
# labels for first, last, phone, and address
label_l_name = tk.Label(root, text="Enter your Last Name:", font=('Arial', 18))
label_l_name.pack()
e_last_name = Entry(root, width=50, borderwidth=3)
e_last_name.pack()
# labels for first, last, phone, and address
label_phone = tk.Label(root, text="Enter your Phone Number including area code:", font=('Arial', 18))
label_phone.pack()
e_phone = Entry(root, width=50, borderwidth=3)
e_phone.pack()
# labels for first, last, phone, and address
label_address = tk.Label(root, text="Enter your Address:", font=('Arial', 18))
label_address.pack()
txt_address = Text(root, height=2, font=('Arial', 16))
txt_address.pack(padx=50)
# continue button to start checking functions
btn_continue = tk.Button(root, text='Continue', command=gather_info, font='Arial, 18')
btn_continue.pack()
# run main program
mainloop()
