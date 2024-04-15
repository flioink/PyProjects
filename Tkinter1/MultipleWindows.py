import tkinter as tk
from tkinter import ttk, messagebox


def ask_yes_no():
    answer = messagebox.askquestion("Title", "body")
    print(answer)
    # messagebox.showinfo("Info Title", "Here is some info!")
    # messagebox.showerror("Info Title", "Here is some info!")


class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("extra window")
        self.geometry("400x300")
        ttk.Label(self, text="A label").pack()
        ttk.Button(self, text="A button").pack()
        ttk.Label(self, text="Another label").pack(expand=True)

    def close_window(self):
        self.destroy()


def create_window():
    global extra_window
    extra_window = Extra()


def close_window():
    extra_window.destroy()


window = tk.Tk()
window.geometry("600x400")
window.title("Multiple windows")

button1 = ttk.Button(window, text="Open main window", command=create_window)
button1.pack(expand=True)
button2 = ttk.Button(window, text="Close main window", command=close_window)
button2.pack(expand=True)
button3 = ttk.Button(window, text="Create yes/no window", command=ask_yes_no)
button3.pack(expand=True)

# loop
window.mainloop()
