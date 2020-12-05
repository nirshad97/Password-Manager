from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 or len(password) > 0:

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"There are he details entered: \nEmail: {email}"
                                               f"\nPassword: {password}\nDo you want to save?")
        if is_ok:
            with open("data.txt", mode='a') as data:
                data.write(f"{website} |{email}| {password}\n")
            website_entry.delete(0, END)  # Everytime we click, add. This would the entries
            password_entry.delete(0, END)  # Deletes everything from index 0 to END

    else:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 90, image=logo_img)
canvas.grid(column=1, row=0)

# Creating Labels

# Creating the Website Label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

# Creating Email Label
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

# Creating Password label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Creating Entry Boxes

# Creating Website entry box
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)  # Spreads component across 2 columns
website_entry.focus()

# Creating Email entry box
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "person@email.com")  # Insert method populates the entry with desired text

# Creating password entry box
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# Creating Buttons

# Creating password button
password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

# Create add button
add_button = Button(text='Add', width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
