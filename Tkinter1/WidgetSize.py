import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Grid")
window.geometry("400x300")
# widgets
label1 = ttk.Label(window, text="Label 1", background="dark red")
label2 = ttk.Label(window, text="Label 2", background="dark blue", width=50)

# layout
# label1.pack()
# label2.pack(fill="x")

# grid
window.columnconfigure((0, 1), weight=1, uniform="a")
window.rowconfigure((0, 1), weight=1, uniform="a")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

# loop
window.mainloop()