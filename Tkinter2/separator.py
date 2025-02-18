from tkinter import *
import ttkbootstrap as tb
import time


def scaler(event):
    pass


root = tb.Window(themename="superhero")
root.title("TTK bootstrap")
root.geometry("500x300")

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_scroll = tb.Scrollbar(my_frame, orient="vertical", bootstyle="dark round")
my_scroll.pack(side="right", fill="y")

# text widget
my_text = Text(my_frame, width=30, height=45,
               yscrollcommand=my_scroll.set,
               wrap="none",
               font=("Helvetica", 18))

my_text.pack()

# config scrollbar
my_scroll.config(command=my_text.yview)


root.mainloop()
