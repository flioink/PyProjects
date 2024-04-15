import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# canvas
canvas = tk.Canvas(window, bg="gray")
canvas.pack()


# canvas.create_rectangle((50, 10, 100, 200), fill="purple", width=3, dash=(4, 2, 1, 1), outline="yellow")
# canvas.create_line((0, 0, 100, 150), fill="blue")
# canvas.create_oval((200, 0, 300, 100), fill="green")
# canvas.create_polygon((0, 0, 100, 200, 300, 50))
# canvas.create_text((100, 100), text="my text")
# canvas.create_window((50, 100), window=ttk.Label(window, text="this is text"))
# canvas.create_arc((200, 0, 300, 100),
#                   fill="red",
#                   start=45,
#                   extent=180,
#                   style=tk.ARC,
#                   outline="yellow",
#                   width=10)


# ex simplified paint app

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size // 2, y - brush_size // 2,
                        x + brush_size // 2, y + brush_size // 2),
                       fill="black")


def brush_size_adj(event):
    global brush_size
    print(event)
    if event.delta > 0:
        brush_size += 2
    else:
        brush_size -= 2

    brush_size = max(0, min(brush_size, 50))


brush_size = 5
canvas.bind("<Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adj)

# loop
window.mainloop()
