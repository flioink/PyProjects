import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class App(ttk.Window):
    def __init__(self, title, size):
        super().__init__(themename="journal")
        self.title("Class based app")
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # loop
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # menu widgets
        menu_button1 = ttk.Button(self, text="Button 1", bootstyle="danger")
        menu_button2 = ttk.Button(self, text="Button 2", bootstyle="success")
        menu_button3 = ttk.Button(self, text="Button 3", bootstyle="dark")

        menu_slider1 = ttk.Scale(self, orient="vertical", bootstyle="info")
        menu_slider2 = ttk.Scale(self, orient="vertical", bootstyle="secondary")

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text="check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text="check 2")
        entry = ttk.Entry(self)

        # grid layout setup
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place the widgets
        menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2, padx=5, pady=5)
        menu_button2.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        entry1 = Entry(self, "Label 1", "Button 1", "red")
        entry2 = Entry(self, "Label 2", "Button 2", "purple")


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, bg_color):
        super().__init__(parent)

        label = ttk.Label(self, text=label_text, background=bg_color)
        button = ttk.Button(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


# if "__name__" == "__main__":
App("Class based app", (600, 600))
