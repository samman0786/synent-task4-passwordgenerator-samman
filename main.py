import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase

    if lower_var.get():
        characters += string.ascii_lowercase

    if number_var.get():
        characters += string.digits

    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror(
            "Error",
            "Please select at least one option"
        )
        return

    length = int(length_entry.get())

    password = ""

    for i in range(length):
        password += random.choice(characters)

    result_label.config(text=password)

window = tk.Tk()

window.title("Synent Technologies Internship Project")

window.geometry("550x500")

window.config(bg="#1e1e1e")

title = tk.Label(
    window,
    text="Synent Technologies",
    font=("Arial", 24, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)

title.pack(pady=10)

subtitle = tk.Label(
    window,
    text="Python Programming Internship",
    font=("Arial", 14),
    fg="white",
    bg="#1e1e1e"
)

subtitle.pack()

project = tk.Label(
    window,
    text="Advanced Password Generator",
    font=("Arial", 18, "bold"),
    fg="lightgreen",
    bg="#1e1e1e"
)

project.pack(pady=20)

length_label = tk.Label(
    window,
    text="Enter Password Length",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
)

length_label.pack()

length_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=20
)

length_entry.pack(pady=10)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

upper_check = tk.Checkbutton(
    window,
    text="Include Uppercase Letters",
    variable=upper_var,
    font=("Arial", 11),
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)

upper_check.pack()

lower_check = tk.Checkbutton(
    window,
    text="Include Lowercase Letters",
    variable=lower_var,
    font=("Arial", 11),
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)

lower_check.pack()

number_check = tk.Checkbutton(
    window,
    text="Include Numbers",
    variable=number_var,
    font=("Arial", 11),
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)

number_check.pack()

symbol_check = tk.Checkbutton(
    window,
    text="Include Special Characters",
    variable=symbol_var,
    font=("Arial", 11),
    fg="white",
    bg="#1e1e1e",
    selectcolor="#1e1e1e"
)

symbol_check.pack(pady=10)

generate_btn = tk.Button(
    window,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="cyan",
    fg="black",
    padx=10,
    pady=5,
    command=generate_password
)

generate_btn.pack(pady=20)

result_title = tk.Label(
    window,
    text="Generated Password",
    font=("Arial", 14, "bold"),
    fg="yellow",
    bg="#1e1e1e"
)

result_title.pack()

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14),
    fg="white",
    bg="#1e1e1e",
    wraplength=450
)

result_label.pack(pady=15)

window.mainloop()