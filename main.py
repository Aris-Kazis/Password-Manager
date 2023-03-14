from tkinter import *

FONT = ("Courier", 12, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    website_entry.delete(0, END)
    email = email_username_entry.get()
    # email_username_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
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
website_entry.config()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_username_entry = Entry(font=FONT)
email_username_entry.config()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "aris7kazis@gmail.com")

password_entry = Entry(font=FONT)
password_entry.config()
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(font=FONT)
generate_password_button.config(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(font=FONT)
add_button.config(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")











window.mainloop()
