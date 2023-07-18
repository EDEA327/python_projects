import json
from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    user_text = website_entry.get()

    with open("passwords.json", "r") as f:
        data = json.load(f)
        try:
            messagebox.showinfo(title="Password Finder",
                                message=f"Website: {user_text} Password: {data[user_text]['password']}")
        except FileNotFoundError:
            messagebox.showinfo(title="Password Finder",
                                message="No data file found")
        except KeyError:
            messagebox.showinfo(title="Password Finder",
                                message=f"No details for the {user_text} exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwordgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username_email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \n Email:{username_email}"
                                               f"\n Password: {password} \n Is it ok to save?")

        if is_ok:
            try:
                with open("passwords.json", "r") as df:
                    # Reading old data
                    data = json.load(df)
            except FileNotFoundError:
                with open("passwords.json", "w") as df:
                    # Creating new data
                    json.dump(new_data, df, indent=4)
            else:
                # Updating the old data with the new data
                data.update(new_data)

                with open("passwords.json", "w") as df:
                    # Saving the updated data
                    json.dump(new_data, df, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
username_email_label = Label(text="Email/Username:", bg="white")
username_email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
username_email_entry = Entry(width=54)
username_email_entry.grid(column=1, row=2, columnspan=2)
username_email_entry.insert(0, "edea@edea.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

add_btn = Button(text="Add", width=46, command=save)
add_btn.grid(column=1, row=4, columnspan=2, pady=5)

generate_password_btn = Button(text="Generate Password", command=passwordgen)
generate_password_btn.grid(column=2, row=3)

search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1, columnspan=2)

window.mainloop()
