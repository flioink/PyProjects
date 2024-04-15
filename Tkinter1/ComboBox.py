import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Spinbox & Combobox")
window.geometry("400x300")

# combobox
items = ("Ice Cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value="scroll down")
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items
combo.pack()

# events

combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text=f"Selected item: {food_string.get()}"))

combo_label = ttk.Label(window, text="Select a food Item")
combo_label.pack()

# spin
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window,
                   from_=3,
                   to=20,
                   increment=1,
                   command=lambda: print("arrow was pressed"),
                   textvariable=spin_int)
spin.pack()
spin.bind("<<Increment>>", lambda event: print("up"))
spin.bind("<<Decrement>>", lambda event: print("down"))

# ex
ex_letters = ("A", "B", "C", "D", "E")
ex_var = tk.StringVar(value="A")
ex_spin = ttk.Spinbox(window, textvariable=ex_var, values=ex_letters)
ex_spin.bind("<<Decrement>>", lambda event: print(ex_var.get()))
ex_spin.pack()

# loop
window.mainloop()
