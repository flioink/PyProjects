import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window

window = ctk.CTk()
window.title("customTkinter")
window.geometry("600x400")

# widgets
string_var = tk.StringVar(value="custom string")
label = ctk.CTkLabel(window,
                     text="CTK label",
                     fg_color=("red", "blue"),
                     text_color=("black", "red"),
                     corner_radius=10,
                     textvariable=string_var)
label.pack()

button = ctk.CTkButton(window,
                       text="CTK Button",
                       fg_color="#FF0",
                       text_color="#000",
                       hover_color="#AA0",
                       command=lambda: ctk.set_appearance_mode("light"))
button.pack()

frame = ctk.CTkFrame(window, fg_color="transparent")
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack()
# exercise
switch = ctk.CTkSwitch(
    window,
    text="Exercise Switch",
    fg_color=("blue", "red"),
    button_color="green",
    button_hover_color="yellow",
    switch_width=60,
    switch_height=30,
    corner_radius=2
)
switch.pack()

# run
window.mainloop()
