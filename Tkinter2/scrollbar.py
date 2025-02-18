from tkinter import *
import ttkbootstrap as tb
import time


def scaler(event):
    my_label.config(text=f"{my_scale.get():.2f}")


root = tb.Window(themename="superhero")
root.title("TTK bootstrap")
root.geometry("500x300")

my_scale = tb.Scale(root,
                    bootstyle="warning",
                    length=300,
                    orient="horizontal",
                    from_=0,
                    to=100,
                    command=scaler)
my_scale.pack(pady=50)

my_label = tb.Label(root, text="0", font=("Helvetica", 18))
my_label.pack()

root.mainloop()
