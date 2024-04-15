import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Menu")
window.geometry("600x400")

# menu

menu = tk.Menu(window)
# sub menu

file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: print("new"))
file_menu.add_command(label="Open", command=lambda: print("open"))
file_menu.add_separator()
menu.add_cascade(label="File", menu=file_menu)

# sub menu 2
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_check_string = tk.StringVar(value="on")
help_menu.add_command(label="Help entry", command=lambda: print(help_check_string.get()))
help_menu.add_checkbutton(label="check", onvalue="on", offvalue="off", variable=help_check_string)

# exercise
ex_menu = tk.Menu(menu, tearoff=False)
ex_menu.add_command(label="Entry 1")
menu.add_cascade(label="Misc", menu=ex_menu)

ex_sub_menu = tk.Menu(menu, tearoff=False)
ex_sub_menu.add_command(label="Entry 1")
ex_menu.add_cascade(label="ex sub menu", menu=ex_sub_menu)

window.configure(menu=menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()
button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="entry 1", command=lambda: print("entry 1"))
button_sub_menu.add_checkbutton(label="check 1")
# menu_button.configure(menu=button_sub_menu)
menu_button["menu"] = button_sub_menu

# loop
window.mainloop()
