import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("button functions & arguments")


# entry
def button_func(entry_string):
    print("Pressed!")
    print(entry_string.get())


def outer_func(param):
    def inner_func():
        print("Pressed!")
        print(param.get())
    return inner_func()


entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="button", command=lambda: button_func(entry_string))
button.pack()

# loop

window.mainloop()
