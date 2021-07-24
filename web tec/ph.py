# Graphical User Interface (GUI)



import tkinter as tk
from tkinter import *



top =tk.Tk()
top.minsize(width=300, height=300)
top.maxsize(width=500, height=500)
top.title('my first GUI')

def clicked():
    data = E1.get()
    L1.config(text = data)


L1 = tk.lable(top,text = ("This is lable")
L1.pack()
E1 = tk.Entry(top)
E1.pack()
B1 = tk.Button(top, text = "press here",
               command = clicked)
              B1.pack()
              top.mainloop()






    
