import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip

# window
window = ttk.Window(themename="darkly")
window.title("Xtra Widgets")

scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill="both")

for i in range(30):
    ttk.Label(scroll_frame, text="Label: {}".format(str(i + 1))).pack(fill="x")
    ttk.Button(scroll_frame, text="Button: {}".format(str(i + 1))).pack(fill="x")

# toast
toast = ToastNotification(title="Msg Title",
                          message="Message",
                          duration=2000,
                          bootstyle="warning",
                          position=(0, 0, "nw"))

button1 = ttk.Button(window, text="Show Toast", command=lambda: toast.show_toast())
button1.pack()

# tooltip
button2 = ttk.Button(window, text="tooltip", bootstyle="warning")
button2.pack(pady=10)

ToolTip(button2, text="a button tooltip", bootstyle="success-inverse")
# calendar

calendar = ttk.DateEntry(window)
calendar.pack(pady=10)

ttk.Button(window, text="get date", command=lambda: print(calendar.entry.get())).pack()

# progress floodgauge
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(
    window,
    text="progress",
    variable=progress_int,
    bootstyle="danger",
    mask="mask {}%")
progress.pack(pady=10, fill="x")
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()

# meter
meter = ttk.Meter(
    window,
    amounttotal=100,
    amountused=10,
    interactive=True,
    metertype="semi",
    subtext="more text",
    bootstyle="danger")


meter.pack(expand=True)

# loop
window.mainloop()