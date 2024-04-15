import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f"x: {event.x}, y: {event.y}")


# window
window = tk.Tk()
window.title("Event Binding")
window.geometry("600x500")

text = tk.Text(window)
text.pack()
entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text="button")
btn.pack()

# events

# btn.bind("<Alt-KeyPress-a>", lambda event: print("an event"))
# window.bind("<Motion>", get_pos)
# window.bind("<KeyPress>", lambda event: print(f"button pressed: {event.char}"))
# entry.bind("<FocusIn>", lambda event: print("entry field selected"))
# entry.bind("<FocusOut>", lambda event: print("entry field unselected"))
# ex
text.bind("<Shift-MouseWheel>", lambda event: print("mousewheel"))

window.mainloop()
