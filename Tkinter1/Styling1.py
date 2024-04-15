import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.geometry("400x300")
window.title("Multiple windows")

# print(font.families())
# print(style.theme_names())

# style
style = ttk.Style()
style.configure("new.TButton", background="purple", font=("Fixedsys", 10))
style.map("new.TButton",
          foreground=[("pressed", "red"), ("disabled", "yellow")],
          background=[("pressed", "green"), ("active", "blue")])

style.configure("TFrame", background="pink")

label = ttk.Label(window,
                  text="A label\n and type some more",
                  background="orange",
                  foreground="white",
                  font=("Fixedsys", 10),
                  justify="center")
label.pack()
button1 = ttk.Button(window, text="Button", style="new.TButton")
button1.pack()
# ex

frame = ttk.Frame(window, style="TFrame", width=100, height=100)
frame.pack(expand=True)

# loop
window.mainloop()
