from tkinter import *
import ttkbootstrap as tb
from PIL import Image

Image.CUBIC = Image.BICUBIC

counter = 5


def clicker():
    global counter
    my_meter.configure(amountused=counter)
    counter += 5
    my_button.configure(text=f"Click {my_meter.amountusedvar.get()}")
    if counter > 100:
        counter = 0


def up():
    if my_meter.amountusedvar.get() < 100:
        my_meter.step(10)


def down():
    if my_meter.amountusedvar.get() >= 10:
        my_meter.step(-10)


root = tb.Window(themename="superhero")
root.title("TTKbootstrap")
root.geometry("500x500")

my_meter = tb.Meter(root,
                    bootstyle="danger",
                    subtext="Tkinter Learned",
                    interactive=True,
                    textright="%",
                    # textleft="$"
                    metertype="full",
                    stripethickness=5,
                    metersize=200,
                    amountused=0,
                    amounttotal=100,
                    subtextstyle="warning"
                    )

my_meter.pack(pady=50)

my_button = tb.Button(root, text="Click here", command=clicker)
my_button.pack(pady=10)

my_button2 = tb.Button(root, text="Step Up", command=up)
my_button2.pack(pady=10)

my_button3 = tb.Button(root, text="Step Down", command=down)
my_button3.pack(pady=10)

root.mainloop()
