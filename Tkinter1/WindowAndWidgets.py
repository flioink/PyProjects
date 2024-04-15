import tkinter as tk
import ttkbootstrap as ttk


def button_function():
    print("Hello!")


# window
window = tk.Tk()
window.title("Window & widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="Test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ex label
label_1 = ttk.Label(master=window, text="my label")
label_1.pack()

# ttk button
button = ttk.Button(master=window, text="A button", command=button_function)
button.pack()

# ex button
my_button1 = ttk.Button(master=window, text="press", command=button_function)
my_button1.pack()

# run
window.mainloop()
