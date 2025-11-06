import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task!")
def delete_task():
    selected = listbox.curselection()
  if selected   
 listbox.delete(selected)
   
 else:
        messagebox.showwarning("Selection Error", "Select a task to delete!")

def update_task():
    selected = listbox.curselection()
    if selected and entry.get():
        listbox.delete(selected)
        listbox.insert(selected, entry.get())
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Update Error", "Select a task and enter updated text!")

root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root, width=40)
entry.pack(padx=5, pady=5)
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(padx=5, pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)
add_btn = tk.Button(frame, text="Add", width=10, command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)
del_btn = tk.Button(frame, text="Delete", width=10, command=delete_task)
del_btn.pack(side=tk.LEFT, padx=5)
update_btn = tk.Button(frame, text="Update", width=10, command=update_task)


update_btn.pack(side=tk.LEFT, padx=5)
root.mainloop()
