import tkinter as tk
import time


root = tk.Tk()
root.title('PyTimer')
root.geometry('400x400')

def start():
    global run
    run = True
    countdown(int(entry.get()))

def countdown(count):
    if run and count>0:
        min , sec = divmod(count,60)
        display.config(text=f"{min:00}:{sec:00}")
        root.after(250,countdown,count-1)
    else:
        display.config(text="TIMES UP!!")

def stop():
    global run
    run = False

def reset():
    stop()
    display.config(text="00:00")
    entry.delete(0,tk.END)

entry = tk.Entry(root,width=10)
entry.grid(row=0,column=1)

label = tk.Label(root,text="Set Time (s):")
label.grid(row=0,column=0)

display = tk.Label(root,text="00:00",font=('Times New Roman',20))
display.grid(row=1,column=0,columnspan=2)

startbtn = tk.Button(root,text="START",command=start)
startbtn.grid(row=2,column=0)

stopbtn = tk.Button(root,text="STOP",command=stop)
stopbtn.grid(row=2,column=1)

resetbtn = tk.Button(root,text="RESET",command=reset)
resetbtn.grid(row=2,column=2)

root.mainloop()