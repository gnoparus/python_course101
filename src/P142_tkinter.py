import tkinter as tk


def button_clicked():
    new_label = tk.Label(window, text="Hello " + entry.get())
    new_label.pack()


window = tk.Tk()
label = tk.Label(window, text="Hello Tkinter")
entry = tk.Entry(window)
button = tk.Button(window, text="OK", command=button_clicked)

label.pack()
entry.pack()
button.pack()

window.mainloop()
