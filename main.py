from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Courier", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------ SAVE PASSWORD --------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------------ FIND PASSWORD --------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \n"
                                                           f"Password: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        print("No Data File Found.")


# --------------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(font=FONT)
website_label.config(text="Website:", padx=10, pady=5)
website_label.grid(column=0, row=1)

email_label = Label(font=FONT)
email_label.config(text="Email/Username:", padx=10, pady=5)
email_label.grid(column=0, row=2)

password_label = Label(font=FONT)
password_label.config(text="Password:", padx=10, pady=5)
password_label.grid(column=0, row=3)

website_entry = Entry(font=FONT)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_username_entry = Entry(font=FONT)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "aris7kazis@gmail.com")

password_entry = Entry(font=FONT)
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(font=FONT)
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(font=FONT)
add_button.config(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(font=FONT)
search_button.config(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
