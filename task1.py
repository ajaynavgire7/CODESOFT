import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
        for task in tasks:
            task_listbox.insert(tk.END, task.strip())


def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")



def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        task_listbox.insert(tk.END, "[Pending] " + task)
        task_entry.delete(0, tk.END)
        save_tasks()


# ----------------------------
# Delete Task
# ----------------------------
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


# ----------------------------
# Mark Task as Completed
# ----------------------------
def mark_completed():
    try:
        selected_task = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task)

        if "[Completed]" not in task_text:
            updated_task = task_text.replace("[Pending]", "[Completed]")
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, updated_task)
            save_tasks()
        else:
            messagebox.showinfo("Info", "Task is already completed.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")



root = tk.Tk()
root.title("To-Do List Application")
root.geometry("450x500")
root.resizable(False, False)


title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)


task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=5)


frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=40, height=12, font=("Arial", 12), yscrollcommand=scrollbar.set)
task_listbox.pack()

scrollbar.config(command=task_listbox.yview)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

complete_button = tk.Button(button_frame, text="Mark Completed", width=15, command=mark_completed, bg="#2196F3", fg="white")
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)


load_tasks()


root.mainloop()
