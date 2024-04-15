import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Hide Widgets")
window.geometry("600x400")


# def toggle_label_place():
#     global label_visibility
#     if label_visibility:
#         label.place_forget()
#         label_visibility = False
#     else:
#         label_visibility = True
#         label.place(relx=0.5, rely=0.5, anchor="center")
#
#
# # place
# button = ttk.Button(window, text="toggle label", command=toggle_label_place)
# button.place(x=10, y=10)
#
# label_visibility = True
# label = ttk.Label(window, text="Label")
# label.place(relx=0.5, rely=0.5, anchor="center")

# grid
# def toggle_label_grid():
#     global label_visibility
#     global label
#     if label_visibility:
#         label.grid_forget()
#         label_visibility = False
#     else:
#         label_visibility = True
#         label.grid(column=1, row=0)
#
#
# window.columnconfigure((0, 1), weight=1, uniform="a")
# window.rowconfigure(0, weight=1, uniform="a")
#
# button = ttk.Button(window, text="toggle label", command=toggle_label_grid)
# button.grid(column=0, row=0)
#
# label_visibility = True
# label = ttk.Label(window, text="Label")
# label.grid(column=1, row=0)

def toggle_label_pack():
    global label_visibility
    if label_visibility:
        label.pack_forget()
        label_visibility = False
        frame.pack(expand=True, before=button)
    else:
        frame.pack_forget()
        label.pack(expand=True, before=button)
        label_visibility = True


# pack


label_visibility = True
label = ttk.Label(window, text="Label")
label.pack(expand=True)

button = ttk.Button(window, text="toggle label", command=toggle_label_pack)
button.pack()

frame = ttk.Frame(window)

# loop
window.mainloop()
