import tkinter as tk

window = tk.Tk()
window.title("Login")
window.geometry("340x440")
window.configure(bg="#333333")

login_label = tk.Label(window, text="Login")
login_label.pack()

window.mainloop()

