import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup

window = tk.Tk()
window.title("Scroll")
window.geometry("600x400")

canvas = tk.Canvas(window, bg="gray", scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 500, fill="green", width=10)

for i in range(100):
    l = randint(0, 2000)
    t = randint(0, 5000)
    r = l + randint(10, 500)
    b = t + randint(10, 500)
    color = choice(("red", "green", "blue", "orange", "yellow", "purple"))
    canvas.create_rectangle(l, t, r, b, fill=color)

canvas.pack(expand=True, fill="both")

# mouse wheel vertical scroll
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

# scrollbar vertical
scrollbar_vertical = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar_vertical.set)
scrollbar_vertical.place(relx=1, rely=0, relheight=1, anchor="ne")

# scrollbar horizontal
scrollbar_horizontal = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_horizontal.set)
scrollbar_horizontal.place(relx=0, rely=1, relwidth=0.975, anchor="sw")

# mouse wheel horizontal scroll
canvas.bind("<Control MouseWheel>", lambda event: canvas.xview_scroll(int(event.delta / 60), "units"))

# run
window.mainloop()
