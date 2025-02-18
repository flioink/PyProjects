from tkinter import *
import ttkbootstrap as tb


def foo(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=x)


root = tb.Window(themename="superhero")
root.title("TTKbootstrap")
root.geometry("500x350")

my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=20)

# basic menu

inside_menu = tb.Menu(my_menu)

# add items

item_var = StringVar()

for i in ["primary", "secondary", "danger", "info", "outline primary", "outline secondary", "outline danger",
          "outline info"]:
    inside_menu.add_radiobutton(label=i, variable=item_var, command=lambda x=i: foo(x))

# associate menu with menubutton

my_menu["menu"] = inside_menu

my_label = tb.Label(root, text="")
my_label.pack(pady=40)

root.mainloop()
