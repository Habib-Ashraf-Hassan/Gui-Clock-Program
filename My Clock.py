from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d,%Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("My Clock")
icon = PhotoImage(file='clock.png')
window.iconphoto(True, icon)
# 3 Labels  for the time,day amd date
time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Comic Sans", 20), fg="blue")
day_label.pack()

date_label = Label(window, font=("Comic Sans", 30), fg="orange")
date_label.pack()

update()

window.mainloop()
