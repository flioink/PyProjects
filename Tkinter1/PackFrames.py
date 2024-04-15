import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Pack")
window.geometry("400x600")
# widgets
# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="First Label", background="dark red")
label2 = ttk.Label(top_frame, text="Label 2", background="dark blue")
# middle widget
label3 = ttk.Label(window, text="Last Label", background="green")
# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text="Last of the Labels", background="orange")
button = ttk.Button(bottom_frame, text="Button")
button2 = ttk.Button(bottom_frame, text="Another Button")

# exercise
ex_frame = ttk.Frame(bottom_frame)
button_ex1 = ttk.Button(ex_frame, text="button 4")
button_ex2 = ttk.Button(ex_frame, text="button 5")
button_ex3 = ttk.Button(ex_frame, text="button 6")

# top layout
label1.pack(side="top", fill="both", expand=True)
label2.pack(side="top", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)
# middle pack
label3.pack(expand=True)

# bottom layout
button.pack(side="left", fill="both", expand=True)
label4.pack(side="left", fill="both", expand=True)
button2.pack(side="left", fill="both", expand=True)
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

# ex layout
button_ex1.pack(side="top", fill="both", expand=True)
button_ex2.pack(side="top", fill="both", expand=True)
button_ex3.pack(side="top", fill="both", expand=True)
ex_frame.pack(side="left", fill="both", expand=True)


# loop
window.mainloop()
