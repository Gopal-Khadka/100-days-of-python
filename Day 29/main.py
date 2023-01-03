from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '.', '-', '_', '@', '#', '$', '%', '&', '*']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password_str = "".join(password_list)
    pyperclip.copy(password_str)
    password.insert(0, password_str)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data=website.get()
    email_data=email.get()
    pass_data=password.get()

    if len(website_data)==0 or len(pass_data)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title=website_data, message=f"These are the details entered:\nEmail:{email_data}\n Password:{pass_data}\n Is it ok to save?")
        if is_ok:
            with open("/home/gopal/Downloads/backup/python/day 29/data.txt","a") as data:
                data.write(f'Website:{website_data} Email:{email_data} Pass:{pass_data}\n')
                password.delete(0,END)
                website.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = Canvas(width=203, height=203)
logo_img = PhotoImage(file="/home/gopal/Downloads/backup/python/day 29/logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

# Website Input
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
website=Entry(width=38)
website.focus()
website.grid(row=1,column=1,columnspan=2)

# Username Input
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
email=Entry(width=38)
email.insert(0,"@gmail.com")
email.grid(row=2,column=1,columnspan=2)
# Password Input
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
password=Entry(width=21)
password.grid(row=3,column=1)

# Pass Generator button
pass_btn=Button(text="Generate Password",width=14,command=generate_password)
pass_btn.grid(row=3,column=2)

# Add to list button
add_btn=Button(text="Add To File",width=36,command=save)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()
