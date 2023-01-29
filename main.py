from tkinter import messagebox
from tkinter import *
from random import *
import pyperclip
import json

auth_accepted = False
AUTH_PASSWORD = "RiverFoxtrotDeltaWither"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    char_list = [choice(letters) for _ in range(nr_letters)]
    sym_list = [choice(symbols) for _ in range(nr_symbols)]
    num_list = [choice(numbers) for _ in range(nr_numbers)]

    password_list = char_list + sym_list + num_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("saved.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("saved.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("saved.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("saved.json", "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.\nPlease add an entry to create the data file.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No entries for {website} found.")


# ---------------------------- UI SETUP ------------------------------- #


# def authenticate():
#    if auth_entry.get() == AUTH_PASSWORD:
#        return True


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# auth_button = Button(text="Confirm Login Password", command=authenticate)
# auth_button.grid(row=1, column=0)

# auth_entry = Entry()
# auth_entry.grid(row=0, column=0)


# if authenticate():
#    auth_accepted = True


# while auth_accepted:
# Logo setup
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


# Widget Setup
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_pw)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=20, command=store_password)
add_button.grid(row=4, column=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
