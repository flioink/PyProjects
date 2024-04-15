import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


def stretch_image(event):
    global resized_tk
    # size
    width = event.width
    height = event.height

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(0, 0, image=resized_tk, anchor="nw")


def fill_image(event):
    global resized_tk
    # curr ratio
    canvas_ratio = event.width / event.height

    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2),
        int(event.height / 2),
        anchor="center",
        image=resized_tk)


def show_full_image(event):
    global resized_tk
    # curr ratio
    canvas_ratio = event.width / event.height

    if canvas_ratio > image_ratio:
        height = int(event.height)
        width = int(height * image_ratio)
    else:
        width = int(event.width)
        height = int(event.width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width / 2),
        int(event.height / 2),
        anchor="center",
        image=resized_tk)


# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Images")
# grid
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure(0, weight=1, uniform="a")

# import image
image_original = Image.open("raccoon.jpg")
image_ratio = image_original.size[0] / image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)
# image tk format
python_dark = Image.open("python_dark.png").resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)
# image ctk format
python_ctk = ctk.CTkImage(
    light_image=Image.open("python_dark.png"),
    dark_image=Image.open("python_light.png"))

# widget
# label = ttk.Label(window, text="racoon", image=image_tk)
# label.pack()
button_frame = ttk.Frame()
button1 = ttk.Button(button_frame, text=" A button", image=python_dark_tk, compound="left")
button1.pack(pady=10)

button2 = ctk.CTkButton(button_frame, text=" A button", image=python_ctk, compound="left")
button2.pack(pady=10)
button_frame.grid(column=0, row=0, sticky="nsew")

# canvas
canvas = tk.Canvas(window, background="gray", bd=0, highlightthickness=0, relief="ridge")
canvas.grid(column=1, columnspan=3, row=0, sticky="nsew")
canvas.create_image(0, 0, image=image_tk, anchor="nw")

canvas.bind("<Configure>", show_full_image)

window.mainloop()
