import tkinter as tk
import ttkbootstrap as ttk


def button_func():
    text = entry.get()
    print(text)
    # update the label
    # label.configure(text="Updated!")
    label["text"] = text
    entry["state"] = "disabled"


def button_func2():
    label["text"] = "some text"
    entry["state"] = "enabled"


# window
window = tk.Tk()
window.title("Getting and Setting Widgets")
window.geometry("400x200")

# widgets
label = ttk.Label(master=window, text="my label")
label.pack()

entry = ttk.Entry(master=window, text="")
entry.pack()

button = ttk.Button(master=window, text="My Button", command=button_func)
button.pack()

# btn2
button = ttk.Button(master=window, text="My Button2", command=button_func2)
button.pack()

# loop
window.mainloop()
