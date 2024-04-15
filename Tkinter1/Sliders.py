import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# setup
window = tk.Tk()
window.title("Sliders")
# window.geometry("320x240")
# sliders
scale_float = tk.DoubleVar(value=15)

scale = ttk.Scale(window,
                  command=lambda value: print(scale_float.get()),
                  from_=0,
                  to=25,
                  length=300,
                  orient="vertical",
                  variable=scale_float)
scale.pack()

# progress bar

progress = ttk.Progressbar(window,
                           variable=scale_float,
                           maximum=25,
                           orient="horizontal",
                           mode="indeterminate",
                           length=400)
progress.pack()

# progress.start(1000)
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=5)
scrolled_text.pack()

# exercise

exercise_int = tk.IntVar()

progress2 = ttk.Progressbar(window,
                            variable=exercise_int,
                            maximum=25,
                            orient="vertical",
                            mode="determinate",
                            length=100)
progress2.pack()

scale2 = ttk.Scale(window,
                   command=lambda value: print(exercise_int.get()),
                   from_=0,
                   to=25,
                   length=100,
                   orient="vertical",
                   variable=exercise_int)

scale2.pack()

label = ttk.Label(window, textvariable=exercise_int)
label.pack()

progress2.start()

# loop
window.mainloop()
