import tkinter as tk
from tkinter import messagebox
import psutil
import os
import datetime

# Log file for OS file system interaction
task_log = "task_log.txt"


# Write logs to file (OS file handling)
def log_action(action):
    with open(task_log, "a") as f:
        f.write(f"{datetime.datetime.now()} - {action}")

# Update OS process count label
def update_process_count():
    process_count = len(psutil.pids())
    process_label.config(text=f"Active OS Processes: {process_count}")

# Add task to list


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        log_action(f"Added task: {task}")
        task_entry.delete(0, tk.END)
        update_process_count()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

# Delete selected task
def delete_task():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)
        task_list.delete(selected)
        log_action(f"Deleted task: {task}")
        update_process_count()
    except:
        messagebox.showerror("Error", "Please select a task to delete")

# Mark selected task as completed
def mark_done():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)
        task_list.delete(selected)
        task_list.insert(selected, task + " ✔")
        log_action(f"Task marked completed: {task}")
        update_process_count()
    except:
        messagebox.showerror("Error", "Select a task to mark done")

# Clear all tasks from the list
def clear_all():
    task_list.delete(0, tk.END)
    log_action("Cleared all tasks")
    update_process_count()


# GUI Window setup
root = tk.Tk()
root.title("Task Manager - OS Project")
root.geometry("360x500")
root.config(bg="lightyellow")


# UI headingtitle 
title = tk.Label(root, text="Task Management System (OS)", font=("Arial", 12, "bold"))
title.pack(pady=10)


# OS Process count
def refresh_process_count():
    update_process_count()
    root.after(3000, refresh_process_count)


process_label = tk.Label(root, text="", bg="lightyellow", font=("Arial", 10, "italic"))
process_label.pack()
update_process_count()
refresh_process_count()


# Entry field for tasks
task_entry = tk.Entry(root, width=32)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, width=20)
add_btn.pack(pady=5)


# Listbox to show tasks
task_list = tk.Listbox(root, width=45, height=15)
task_list.pack(pady=10)


# Action buttons
mark_btn = tk.Button(root, text="Mark as Done", command=mark_done, width=20)
mark_btn.pack(pady=2)


delete_btn = tk.Button(root, text="Delete Task", command=delete_task, width=20)
delete_btn.pack(pady=2)


clear_btn = tk.Button(root, text="Clear All", command=clear_all, width=20)
clear_btn.pack(pady=2)


root.mainloop()
