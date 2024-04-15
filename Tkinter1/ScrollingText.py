import tkinter as tk
from tkinter import ttk

# setup

window = tk.Tk()
window.title("Text Scroll")
window.geometry("600x400")

text = tk.Text(window)
for i in range(1, 200):
    text.insert(f"{i}.0", f"text: {i}\n")
text.pack(expand=True, fill="both")

# text scroll vertical
scroll_text = ttk.Scrollbar(window, orient="vertical", command=text.yview)
text.configure(yscrollcommand=scroll_text.set)
scroll_text.place(relx=1, rely=0, relheight=1, anchor="ne")

# run
window.mainloop()
