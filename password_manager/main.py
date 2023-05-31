from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()

    website_entry.delete(0, END)
    username_email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white",highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

username_email_label = Label(text="Email/Username:", bg="white")
username_email_label.grid(column=0, row=2)
username_email_entry = Entry(width=35)
username_email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=2,)

add_btn = Button(text="Add", highlightthickness=0, width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

generate_password_btn = Button(text="Generate Password", highlightthickness=0)
generate_password_btn.grid(column=2, row=3)

window.mainloop()
