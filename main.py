import time
from tkinter import *

# ------------------- Program Logic ------------------- #
time_started = time.time()
last_digit_time = 0
deleting = False


def on_press(event):
    global last_digit_time
    last_digit_time = time.time()
    window.after(3000, delete)


def delete():
    global deleting, last_digit_time
    if not deleting and time.time() - last_digit_time > 3:
        deleting = True
        user_box.delete("1.0", "end")
        deleting = False


# ------------------- UI ------------------- #

window = Tk()
window.title("Disappearing Text")
window.config(padx=20, pady=20)

user_box = Text(window, padx=20, pady=20, height=5, font=("Helvetica", 16))
user_box.grid(column=0, row=2, columnspan=2)

window.bind_all('<Key>', on_press)

window.mainloop()
