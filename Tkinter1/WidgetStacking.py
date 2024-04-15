import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Stacking order")
window.geometry("400x400")

# widgets
label1 = ttk.Label(window, text="Label 1", background="dark red")
label2 = ttk.Label(window, text="Label 2", background="dark blue")
label3 = ttk.Label(window, text="Label 3", background="pink")


button1 = ttk.Button(window, text="Button 1", command=lambda: label1.tkraise(aboveThis=label2))
button2 = ttk.Button(window, text="Button 2",  command=lambda: label2.tkraise())
button3 = ttk.Button(window, text="Button 3",  command=lambda: label3.tkraise())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=150, y=30, width=140, height=100)
button1.place(rely=1, relx=0.8, anchor="se")
button2.place(rely=1, relx=1, anchor="se")
button3.place(rely=0.9, relx=1, anchor="se")


# loop
window.mainloop()