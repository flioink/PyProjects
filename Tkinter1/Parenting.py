import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Frames and parenting")
window.geometry("600x400")

# frame

frame = ttk.Frame(window,
                  width=100,
                  height=200,
                  borderwidth=10,
                  relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="left")

# master setting
label = ttk.Label(frame, text="Label")
label.pack()
button = ttk.Button(frame, text="Button")
button.pack()

# example
label2 = ttk.Label(window, text="Label outside")
label2.pack()

# exercise
frame2 = ttk.Frame(window,
                   width=100,
                   height=200,
                   borderwidth=10,
                   relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side="right")

label3 = ttk.Label(frame2, text="Label Right")
label3.pack()

button2 = ttk.Button(frame2, text="Button")
button2.pack()

ttk.Entry(frame2).pack()

# run
window.mainloop()
