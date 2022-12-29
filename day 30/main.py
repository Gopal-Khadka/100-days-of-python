from textwrap import indent
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json
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
    password.insert(0, password_str)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data=website.get()
    email_data=email.get()
    pass_data=password.get()
    new_data={
        website_data.title():{
            "email":email_data,
            "password":pass_data
        }

    }

    if len(website_data)==0 or len(pass_data)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty.")
    else:
        try:
            with open("/home/gopal/Downloads/backup/python/day 29/data.json","r") as data_file:
                wdata=json.load(data_file) #read file
        except FileNotFoundError:
                with open("/home/gopal/Downloads/backup/python/day 29/data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)#dump new data in file
        else:
            wdata.update(new_data)#update the existing file
            with open("/home/gopal/Downloads/backup/python/day 29/data.json","w") as data_file:
                json.dump(wdata,data_file,indent=4) #write inside file

        password.delete(0,END)
        website.delete(0,END)
#-----------------------------FIND DATA--------------------------------#
def find_data():
    webs=website.get()
    web=webs.title()
    try:
        with open("/home/gopal/Downloads/backup/python/day 29/data.json") as data_file:
            data=json.load(data_file)
    except:
        messagebox.showinfo(title="Error",message="No data file found.")

    else:
        if web in data:
            email=data[web]["email"]
            password=data[web]["password"]
            messagebox.showinfo(title=f"{web}",message=f"Email:{email} \n Password: {password}")

        else:
            messagebox.showinfo(title="Error",message=f"No data for {web} exsits.")






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
website=Entry(width=21)
website.focus()
website.grid(row=1,column=1,columnspan=1)

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

#search button
search_btn=Button(text="Search",width=14,command=find_data)
search_btn.grid(row=1,column=2)

# Add to list button
add_btn=Button(text="Add To File",width=36,command=save)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()
