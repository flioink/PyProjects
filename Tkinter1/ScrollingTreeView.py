import tkinter as tk
from tkinter import ttk
from random import choice

# setup

window = tk.Tk()
window.title("Text Scroll")
window.geometry("600x400")

# treeview
table = ttk.Treeview(window, columns=(1, 2), show="headings")
table.heading(1, text="First name")
table.heading(2, text="Last name")

first_names = ["Bob", "Maria", "Jim", "Lisa", "Ana", "Maria", "Henry", "John", "Jack"]
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

for i in range(100):
    table.insert(parent="", index=tk.END, values=(choice(first_names), choice(last_names)))

table.pack(expand=True, fill="both")

scrollbar_table = ttk.Scrollbar(window, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor="ne")

# run
window.mainloop()
