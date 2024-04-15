import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Grid")
window.geometry("400x600")

# widgets
label1 = ttk.Label(window, text="Label 1", background="dark red")
label2 = ttk.Label(window, text="Label 2", background="dark blue")
label3 = ttk.Label(window, text="Label 3", background="green")
button1 = ttk.Button(window, text="Button 1")
# layout
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button1.place(relx=1, rely=1, anchor="se")
# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text="Frame label", background="yellow")
frame_button = ttk.Button(frame, text="Frame button")

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# ex
label4 = ttk.Label(window, text="Label 4", background="purple")
label4.place(relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor="center")

# loop
window.mainloop()