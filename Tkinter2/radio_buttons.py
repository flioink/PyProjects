from tkinter import *
import ttkbootstrap as tb
import time


def increment():
    my_progress["value"] += 20
    my_label.config(text=my_progress["value"])


def start():
    my_progress.start(10)


def stop():
    my_progress.stop()


def auto():
    for x in range(5):
        my_progress["value"] += 20
        my_label.config(text=my_progress["value"])
        # update one at a time
        root.update_idletasks()
        time.sleep(1)


root = tb.Window(themename="superhero")
root.title("TTK bootstrap")
root.geometry("500x300")

my_progress = tb.Progressbar(
    root,
    bootstyle="danger",
    maximum=100,
    mode="determinate",
    length=300,
    value=0
)

my_progress.pack(pady=40)

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_button = tb.Button(my_frame, text="Increment 20", bootstyle="info", command=increment)
my_button.grid(column=0, row=0, padx=10)

my_button1 = tb.Button(my_frame, text="Start", bootstyle="info", command=start)
my_button1.grid(column=1, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="Stop", bootstyle="info", command=stop)
my_button2.grid(column=2, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="Auto", bootstyle="info", command=auto)
my_button3.grid(column=3, row=0, padx=10)

my_label = tb.Label(root, text="")
my_label.pack()

root.mainloop()
