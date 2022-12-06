import tkinter as tk
from tkinter import ttk





root = tk.Tk()
root.title("BULB OFF/ON")
root.geometry("300x300")




img1 = tk.PhotoImage(file='bulboff.gif')

lb1 = ttk.Label(root , image=img1)
lb1.pack(ipady=20)


def b_off():
    img1.config(file='bulboff.gif')
def b_on():
    img1.config(file='bulbon.gif')

btn1= ttk.Button(root,text="ON" , command= b_on)
btn1.place(x=150,y=250)

btn2= ttk.Button(root,text="OFF" , command= b_off)
btn2.place(x=50,y=250)





root.mainloop()
