import tkinter as tk
import time
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x650")
root.config(bg='burlywood1')
name_var = tk.StringVar()


def myClick():
    text.set("here is the text try to test your speed by typing this one and compare theme ")
    entry1 = tk.Entry(root, textvariable=name_var, width=40, font=('Arial 24')).pack(pady=20)
    butttext.set("finish")
    count()


def c():
    name = name_var.get()
    t="here is the text try to test your speed by typing this one and compare theme "
    for l in name:
        for n in t:
            if l==n:
                m="you are so fast great!"
            else:
                m="try again you have some mistakes "
    tk.messagebox.showinfo(message=f"{m}")


def count():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        # Update the time
        root.update()
        time.sleep(1)
        if (times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')

        times -= 1
    c()


sec = tk.StringVar()
tk.Entry(root, textvariable=sec, width=2, font='Helvetica 14').place(x=280, y=200)
sec.set('10')

mins = tk.StringVar()
tk.Entry(root, textvariable=mins, width=2, font='Helvetica14').place(x=250, y=200)
mins.set('00')
hrs = tk.StringVar()
tk.Entry(root, textvariable=hrs, width=2, font='Helvetica 14').place(x=220, y=200)
hrs.set('00')
text = tk.StringVar()
text.set(" the text will appear here ")

label = tk.Label(root, textvariable=text)
label.pack(pady=20)
butttext = tk.StringVar()
butttext.set("here is the sped test when you click this button the text will appear")
button = tk.Button(root, textvariable=butttext, command=myClick)
button.pack(pady=10)

root.mainloop()
