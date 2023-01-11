import tkinter as tk

window = tk.Tk()
label = tk.Label(window, text="Hello Tkinter")
entry = tk.Entry(window)
button = tk.Button(window, text="OK")

label.pack()
entry.pack()
button.pack()

window.mainloop()
