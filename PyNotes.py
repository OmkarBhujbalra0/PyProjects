import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


root = tk.Tk()
root.title('PyNotes')

def save():
    path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[('Text Files',"*.txt"),("All Files","*.*")])

    if path:
        with open(path,'w') as file:
            file.write(text_area.get("1.0",tk.END))
        messagebox.showinfo('Success','Note Saved Successfully!!')

def load():
    path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[('Text Files',"*.txt"),("All Files","*.*")])

    if path:
        with open(path,'r') as file:
            text_area.delete("1.0",tk.END)
            text_area.insert(tk.END,file.read())

def clear():
    text_area.delete("1.0",tk.END)

text_area = tk.Text(root,wrap=tk.WORD,height=15,width=50)
text_area.pack(padx=10,pady=10)

bframe = tk.Frame(root)
bframe.pack(pady=10)

savebtn = tk.Button(bframe,text="Save",command=save)
savebtn.pack(side=tk.LEFT,padx=5)

loadbtn = tk.Button(bframe,text='Load',command=load)
loadbtn.pack(side=tk.LEFT,padx=5)

clearbtn = tk.Button(bframe,text='Clear',command=clear)
clearbtn.pack(side=tk.LEFT,padx=5)

root.mainloop()