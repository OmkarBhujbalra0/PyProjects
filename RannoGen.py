import tkinter as tk
import random

root = tk.Tk()
root.title('Random Numerical Genesis')
root.geometry('400x400')

label = tk.Label(root,text="Click to generate a random number:",font=('Times New Roman',30))
label.pack(pady=10)

result = tk.Label(root,text="",font=('Times New Roman',25))
result.pack(pady=10)

def genesis():
    randomnum = random.randint(1,100)
    result.config(text=str(randomnum))

generate = tk.Button(root,text="Generate",command=genesis,font=('Times New Roman',20))
generate.pack(pady=10)
root.mainloop()