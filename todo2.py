import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Initialize the main window
window = tk.Tk()
window.title("TODO-IT")
window.geometry("500x600")
window.configure(bg="white")

# Load background image
bg_image = tk.PhotoImage(file=r"C:\Users\Admin\Desktop\mbg.png")  
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  

# List to store tasks
tasks = []

# Functions
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def edit_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        current_task = tasks[selected_task_index]
        entry_task.delete(0, tk.END)
        entry_task.insert(0, current_task)
        delete_task()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

def mark_complete():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        completed_task = tasks[selected_task_index]
        tasks[selected_task_index] = f"{completed_task} (Completed)"
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, tasks[selected_task_index])
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Save Successful", "Tasks saved successfully!")

def load_tasks():
    global tasks
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
        messagebox.showinfo("Load Successful", "Tasks loaded successfully!")

# buttons
frame = tk.Frame(window, bg="lightblue")
frame.pack(pady=20)

entry_task = tk.Entry(frame, font=("Arial", 16), width=30)
entry_task.pack(side=tk.LEFT, padx=10)

btn_add = tk.Button(frame, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 12))
btn_add.pack(side=tk.LEFT)

listbox_tasks = tk.Listbox(window, font=("Arial", 14), width=30, height=10)
listbox_tasks.pack(pady=20)

btn_edit = tk.Button(window, text="Edit Task", command=edit_task, bg="blue", fg="white", font=("Arial", 12))
btn_edit.pack(pady=5)

btn_delete = tk.Button(window, text="Delete Task", command=delete_task, bg="red", fg="white", font=("Arial", 12))
btn_delete.pack(pady=5)

btn_complete = tk.Button(window, text="Mark as Complete", command=mark_complete, bg="purple", fg="white", font=("Arial", 12))
btn_complete.pack(pady=5)

frame_save_load = tk.Frame(window, bg="grey")
frame_save_load.pack(pady=20)

btn_save = tk.Button(frame_save_load, text="Save Tasks", command=save_tasks, bg="pink", fg="black", font=("Arial", 12))
btn_save.pack(side=tk.LEFT, padx=10)

btn_load = tk.Button(frame_save_load, text="Load Tasks", command=load_tasks, bg="pink", fg="black", font=("Arial", 12))
btn_load.pack(side=tk.LEFT, padx=10)

# Run the main loop
window.mainloop()
