import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61

    output_string.set(str(km_output))


# window
window = ttk.Window(themename="darkly")
window.title("Demo")
window.geometry("300x150")

# title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="convert", command=convert)
entry.pack(side="left", padx=5)
button.pack(side="left")
input_frame.pack(pady=10)

# output label
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text="output",
                         font="Calibri 24",
                         textvariable=output_string)
output_label.pack(padx=10)

# run
window.mainloop()
