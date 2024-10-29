import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('CheckBocs')
root.geometry('400x400')

def add():
    task = entry.get()
    if task:
        l.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning('Please enter anything!')

def remove():
    try:
        taskindex = l.curselection()[0]
        l.delete(taskindex)
    except:
        messagebox.showwarning('Please select task!')


header = tk.Label(root,text="CheckBocs",anchor='center',font=('Tahoma',30))
header.pack()

entry = tk.Entry(root,font=('Tohama',30))
entry.pack(pady=20)

l = tk.Listbox(root,font=('Tohama',20),selectmode=tk.SINGLE)
l.pack(pady=10,fill=tk.BOTH,expand=True)

addon = tk.Button(root,text="Add Task",font=('Tohama',15),command=add)
addon.pack(pady=5)
removon = tk.Button(root,text="Remove Task",font=('Tohama',15),command=remove)
removon.pack(pady=5)


root.mainloop()