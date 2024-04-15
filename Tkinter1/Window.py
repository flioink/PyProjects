import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Menu")
# window.geometry("600x400")
window.iconbitmap("test.ico")

# window sizes
window.minsize(200, 100)
# window.maxsize(1024, 768)
window.resizable(True, True)

# ex
window_width = 1400
window_height = 600

display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - display_height / 2)

window.geometry(f"{window_width}x{window_height}+{left}+{top}")

# screen attrs
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes("-alpha", 1)
# always on top
window.attributes("-topmost", True)

# security event
window.bind("<Escape>", lambda event: window.quit())
# disable window interaction
# window.attributes("-disable", True)

# full screen
# window.attributes("-fullscreen", True)

# title bar hiding
# window.overrideredirect(True)

# grip handles
grip = ttk.Sizegrip(window)
grip.pack()
grip.place(relx=1.0, rely=1.0, anchor="se")

# loop
window.mainloop()