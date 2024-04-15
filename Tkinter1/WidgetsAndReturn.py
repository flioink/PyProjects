import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
    # widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew")
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nsew")

    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, ex_button):
        super().__init__(master=parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew")

        self.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_text(ex_button).grid(row=0, column=2, sticky="nsew")

    def create_text(self, btn_text):

        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand=True, fill="both")
        ttk.Button(frame, text=btn_text).pack(expand=True, fill="both")

        return frame





# window
window = tk.Tk()
window.title("Widgets & Return")
window.geometry("400x600")

# widgets
Segment(window, "label", "button", "one")
Segment(window, "test", "click", "two")
Segment(window, "hello", "test", "three")
Segment(window, "test", "click", "four")
Segment(window, "hello", "test", "five")

# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)


# loop
window.mainloop()
