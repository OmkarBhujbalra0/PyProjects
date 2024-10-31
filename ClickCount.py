import tkinter as tk

root = tk.Tk()
root.title('CliKounter')
root.geometry('400x400')

header = tk.Label(root,text="CliKounter",font=('Impact',30))
header.pack(pady=10)

para = tk.Label(root,text="Click to count your clicks!",font=('Ariel',15))
para.pack(pady=10)

c = 0

def count():
    global c
    c+=1
    displayc.config(text=f"Number of Clicks : {c}")

def reset():
    global c
    c = 0
    displayc.config(text=f"Number of Clicks : 0")

displayc = tk.Label(root,text="Number of Clicks : 0",font=('Agency',25))
displayc.pack(pady=10)

update = tk.Button(root,text="Click",command=count,width=15,height=5)
update.pack(pady=10)

reset = tk.Button(root,text="Reset",command=reset,width=15,height=5)
reset.pack(pady=10)

root.mainloop()