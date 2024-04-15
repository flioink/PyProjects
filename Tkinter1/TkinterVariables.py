import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("button_pressed")

# window
window = tk.Tk()
window.title("Tkinter variables")
# window.geometry("240x240")

# tkiner variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master=window, text="hi", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, text="", textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

# ex
string_var2 = tk.StringVar(value="test")

entry1 = ttk.Entry(master=window, text="", textvariable=string_var2)
entry1.pack()

entry2 = ttk.Entry(master=window, text="", textvariable=string_var2)
entry2.pack()

label2 = ttk.Label(master=window, text="", textvariable=string_var2)
label2.pack()

# loop
window.mainloop()