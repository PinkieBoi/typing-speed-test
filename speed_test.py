# Keyboard image from Vecteezy (https://www.vecteezy.com/free-png/laptop)
from tkinter import *
from random import choice
from PIL import Image, ImageTk
from typing_texts import texts
from tkinter.messagebox import showinfo


def display_score(score):
    showinfo(title="Typing Speed Score", message=f"You type at {score} words per minute!")


FONT = ("Ubuntu", 14, "normal")

win = Tk()
win.title = "Typing Speed"
canvas = Canvas(win, width=800)
keyboard_img = ImageTk.PhotoImage(image=Image.open("assets/keyboard_illustration.png").resize((800, 250)))
img = canvas.create_image(0, 0, image=keyboard_img, anchor=NW)
canvas.grid(row=1, column=0)
text = Label(text=choice(texts), font=FONT)
text.grid(row=0, column=0)

if __name__ == "__main__":
    win.mainloop()
