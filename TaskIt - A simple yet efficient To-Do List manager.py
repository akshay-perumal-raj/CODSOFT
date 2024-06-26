import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

def complete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, f"{task_text}    ✔")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

root = tk.Tk()
root.title("TaskIt - a simple yet efficient To-Do List manager")
root.geometry("500x600")

heading_label = tk.Label(root, text="Task List", font=("Helvetica", 18, "bold"))
heading_label.pack(pady=10)

tagline_label = tk.Label(root, text="Don't put off until tomorrow what you can do today.", font=("Helvetica", 12))
tagline_label.pack(pady=5)

instructions_label = tk.Label(root, text="Instructions:\n"
                                         " - Add tasks by typing in the box above and pressing Enter.\n"
                                         " - Select a task and press Delete to remove it.\n"
                                         " - Press Enter when a task is selected to mark it as completed.", 
                              justify=tk.LEFT)
instructions_label.pack(pady=10, padx=10)


tasks_listbox = tk.Listbox(root, width=50, height=15, activestyle='none')
tasks_listbox.pack(pady=10)

enter_task_label = tk.Label(root, text="Enter your tasks below", font=("Helvetica", 10))
enter_task_label.pack()

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

task_entry.bind("<Return>", add_task)
tasks_listbox.bind("<Delete>", delete_task)
tasks_listbox.bind("<Return>", complete_task)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

add_task_button = tk.Button(control_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)

delete_task_button = tk.Button(control_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)

clear_tasks_button = tk.Button(control_frame, text="Clear All Tasks", command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT, padx=5)

complete_task_button = tk.Button(control_frame, text="Complete Task", command=complete_task)
complete_task_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
