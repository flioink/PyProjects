import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tabs")
window.geometry("600x400")

# notebook widget
notebook = ttk.Notebook(window)
# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button 1")
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="Text in tab 2")
label2.pack()
button2 = ttk.Button(tab2, text="Button 2")
button2.pack()
entry2 = ttk.Entry(tab2, text="")
entry2.pack()

# tab 3
tab3 = ttk.Frame(notebook)
button3 = ttk.Button(tab3, text="Button 3")
button3.pack()
button4 = ttk.Button(tab3, text="Button 4")
button4.pack()
label3 = ttk.Label(tab3, text="Label 3")
label3.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")
notebook.pack()

# loop
window.mainloop()
