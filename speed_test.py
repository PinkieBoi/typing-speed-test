# Keyboard image from Vecteezy (https://www.vecteezy.com/free-png/laptop)
from tkinter import *
from random import choice
from datetime import time
from PIL import Image, ImageTk
from typing_texts import texts
from tkinter.messagebox import showinfo, askyesno


def start_typing():
    pass


def end_test():
    pass


def get_time():
    pass


def display_score(score):
    showinfo(title="Typing Speed Score", message=f"You type at {score} words per minute!")


FONT = ("Ubuntu", 14, "normal")

start_time = None
end_time = None
win = Tk()
win.title = "Typing Speed"
canvas = Canvas(win, width=800)
keyboard_img = ImageTk.PhotoImage(image=Image.open("assets/keyboard_illustration.png").resize((800, 250)))
img = canvas.create_image(0, 0, image=keyboard_img, anchor=NW)
text = Label(text=choice(texts), font=FONT)
start_btn = Button(text="Start Typing", command=start_typing)
end_btn = Button(text="End Test", command=end_test)
# to_type = list(text)

# Place components in window
text.grid(row=0, column=0, columnspan=2)
canvas.grid(row=1, column=0, columnspan=2)
start_btn.grid(row=2, column=0)
end_btn.grid(row=2, column=1)

if __name__ == "__main__":
    win.mainloop()
