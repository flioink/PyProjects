from tkinter import *
import ttkbootstrap as tb
import time


def clicker():
    my_label.config(text=f"You selected: {my_topping.get()}")


root = tb.Window(themename="superhero")
root.title("TTK bootstrap")
root.geometry("500x500")

toppings = ["Pepperoni", "Cheese", "Veggie"]

# Tkinter var to track
my_topping = StringVar()

for topping in toppings:
    tb.Radiobutton(root, bootstyle="danger", variable=my_topping, text=topping, value=topping, command=clicker).pack(pady=10)

my_button = tb.Button(root, text="Click here", command=clicker)
my_button.pack(pady=20)

my_label = tb.Label(root, text="You selected: ")
my_label.pack()

# Radio buttons
rb1 = tb.Radiobutton(root,
                     bootstyle="info toolbutton",
                     variable=my_topping,
                     text="Radio Button 1",
                     value="Radio Button 1",
                     command=clicker)
rb1.pack(pady=20)

rb2 = tb.Radiobutton(root,
                     bootstyle="info toolbutton",
                     variable=my_topping,
                     text="Radio Button 2",
                     value="Radio Button 2",
                     command=clicker)
rb2.pack(pady=20)

root.mainloop()
