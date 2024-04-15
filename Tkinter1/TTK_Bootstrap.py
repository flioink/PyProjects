import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# window
window = ttk.Window(themename="cyborg")
window.title("ttk bootstrap intro")
window.geometry("400x500")

label = ttk.Label(window, text="Label 1")
label.pack(pady=10)

b1 = ttk.Button(window, text='primary', bootstyle=PRIMARY)
b1.pack(side=TOP, padx=5, pady=5)

b2 = ttk.Button(window, text='secondary', bootstyle=SECONDARY)
b2.pack(side=TOP, padx=5, pady=5)

b3 = ttk.Button(window, text='success', bootstyle=SUCCESS)
b3.pack(side=TOP, padx=5, pady=5)

b4 = ttk.Button(window, text='info', bootstyle=INFO)
b4.pack(side=TOP, padx=5, pady=5)

b5 = ttk.Button(window, text='warning', bootstyle=WARNING)
b5.pack(side=TOP, padx=5, pady=5)

b6 = ttk.Button(window, text='danger', bootstyle=DANGER)
b6.pack(side=TOP, padx=5, pady=5)

b7 = ttk.Button(window, text='light', bootstyle=LIGHT)
b7.pack(side=TOP, padx=5, pady=5)

b8 = ttk.Button(window, text='dark', bootstyle=DARK)
b8.pack(side=TOP, padx=5, pady=5)

# loop
window.mainloop()