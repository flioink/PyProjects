import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # anim logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_fwd()
        else:
            self.animate_bwd()

    def animate_fwd(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_fwd)
        else:
            self.in_start_pos = False

    def animate_bwd(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_bwd)
        else:
            self.in_start_pos = True


def move_btn():
    global button_x
    button_x += 0.01
    button.place(relx=button_x, rely=0.5, anchor="center")

    if button_x < 0.9:
        print(button_x)
        window.after(10, move_btn)

    # colors = ["red", "yellow", "pink", "green", "gray"]
    # color = choice(colors)
    # button.configure(fg_color=color)


# setup
window = ctk.CTk()
window.geometry("600x400")
window.title("Animated widgets")

# animated wget
animated_panel = SlidePanel(window, 1, 0.7)
ctk.CTkLabel(animated_panel, text="Label 1").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkLabel(animated_panel, text="Label 2").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkButton(animated_panel, text="Button", corner_radius=0).pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkTextbox(animated_panel, fg_color=("#dbdbdb", "#2b2b2b")).pack(expand=True, fill="both", pady=10)

# button
button_x = 0.5
button = ctk.CTkButton(window, text="Toggle sidebar", command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor="center")

# loop
window.mainloop()
