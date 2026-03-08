from tkinter import *
import random
import string

root = Tk()
root.title("My Password Maker")
root.geometry("420x320")
root.configure(bg="#2b2b2b")

password_var = StringVar()

def generate_password():
    length = int(length_box.get())
    chars = ""

    if upper_var.get() == 1:
        chars += string.ascii_uppercase
    if lower_var.get() == 1:
        chars += string.ascii_lowercase
    if num_var.get() == 1:
        chars += string.digits
    if sym_var.get() == 1:
        chars += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(chars)

    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

title = Label(root,text="Password Generator",
              font=("Arial",18,"bold"),
              bg="#2b2b2b",fg="white")
title.pack(pady=10)

frame = Frame(root,bg="#2b2b2b")
frame.pack(pady=10)

Label(frame,text="Password Length:",bg="#2b2b2b",
      fg="white",font=("Arial",11)).grid(row=0,column=0,padx=5)

length_box = Entry(frame,width=8,font=("Arial",11),justify="center")
length_box.grid(row=0,column=1)
length_box.insert(0,"10")

upper_var = IntVar(value=1)
lower_var = IntVar(value=1)
num_var = IntVar(value=1)
sym_var = IntVar()

Checkbutton(root,text="Uppercase Letters",
            variable=upper_var,bg="#2b2b2b",
            fg="white",selectcolor="#2b2b2b").pack()

Checkbutton(root,text="Lowercase Letters",
            variable=lower_var,bg="#2b2b2b",
            fg="white",selectcolor="#2b2b2b").pack()

Checkbutton(root,text="Numbers",
            variable=num_var,bg="#2b2b2b",
            fg="white",selectcolor="#2b2b2b").pack()

Checkbutton(root,text="Symbols",
            variable=sym_var,bg="#2b2b2b",
            fg="white",selectcolor="#2b2b2b").pack()

Button(root,text="Generate Password",
       font=("Arial",11),
       bg="#4CAF50",fg="white",
       command=generate_password).pack(pady=10)

Entry(root,textvariable=password_var,
      font=("Arial",13),
      width=28,
      justify="center").pack(pady=5)

Button(root,text="Copy",
       font=("Arial",10),
       bg="#2196F3",fg="white",
       command=copy_password).pack(pady=5)

root.mainloop()
