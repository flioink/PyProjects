import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry("600x400")

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(window, columns=("first", "last", "email"), show="headings")

table.heading("first", text="First Name")
table.heading("last", text="Last Name")
table.heading("email", text="E-mail")

# table.insert(parent, index, values, )

for i in range(30):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}_{last}@gmail.com"
    data = (first, last, email)
    table.insert(parent="", index=0, values=data)

table.pack(fill="both", expand=True)

table.insert(parent="", index=tk.END, values=("XXX", "YYY", "ZZZ"))


# events

def item_select(_):
    for i in table.selection():
        print(table.item(i)["values"])

    # table.item(table.selection())


# deleting items

def del_items(_):
    for item in table.selection():
        table.delete(item)


table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", del_items)

# loop
window.mainloop()
