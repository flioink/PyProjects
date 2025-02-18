from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
root.title("TTK bootstrap")
root.geometry("500x500")

my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = tb.Label(tab1, text="My Label1", font=("Helvetica", 18))
my_label.pack(pady=20)

my_text = Text(tab1, width=70, height=10)
my_text.pack(pady=20, padx=10)

my_button = tb.Button(tab1, text="Click Me!", bootstyle="danger outline")
my_button.pack(pady=20)

my_label2 = tb.Label(tab2, text="Tab 2", font=("Helvetica", 18))
my_label2.pack(pady=20)
# add frames to notebook
my_notebook.add(tab1, text="Tab One")
my_notebook.add(tab2, text="Tab Two")

root.mainloop()
