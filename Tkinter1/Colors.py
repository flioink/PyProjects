import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.geometry("400x300")
window.title("Colors")

ttk.Label(window, background="yellow").pack(expand=True, fill="both")
ttk.Label(window, background="#2ba55e").pack(expand=True, fill="both")
ttk.Label(window, background="#753f2d").pack(expand=True, fill="both")


# loop
window.mainloop()
