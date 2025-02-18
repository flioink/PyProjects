from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


def foo():
    pass


root = tb.Window(themename="superhero")
root.title("TTKbootstrap")
root.geometry("500x350")

my_frame = tb.Frame(root, bootstyle="light")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, text="click me", bootstyle="dark", command=foo)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Hello, there!", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()
