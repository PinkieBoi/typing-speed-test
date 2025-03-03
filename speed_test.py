# Keyboard image from Vecteezy (https://www.vecteezy.com/free-png/laptop)
import time
from tkinter import *
from random import choice
from typing_texts import texts
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo, askyesno


def start_typing():
    global start_time
    textbox.grid(row=1, column=0, columnspan=2)
    start_time = time.clock_gettime(1)
    return start_time


def end_test():
    global start_time
    end_time = time.clock_gettime(1)
    time_taken = round(end_time - start_time, 2)
    display_score(time_taken)


def get_time():
    global start_time
    start_time = time.clock_gettime(1)
    return start_time


def display_score(score):
    global text
    words = len(text.split())
    wpm_score = round(words / (score / 60))
    showinfo(
        title="Well done!",
        message=f"You managed {wpm_score} words per minute!\nWould you like to try again?"
    )
    exit()


FONT = ("Ubuntu", 14, "normal")

start_time = None
testing = True
win = Tk()
win.title = "Typing Speed"
canvas = Canvas(win, width=800)
keyboard_img = ImageTk.PhotoImage(image=Image.open("assets/keyboard_illustration.png").resize((800, 250)))
img = canvas.create_image(0, 0, image=keyboard_img, anchor=NW)
text = choice(texts)
text_label = Label(text=text, font=FONT)
textbox = Text(font=FONT, height=8)
start_btn = Button(text="Start Typing", command=start_typing)
end_btn = Button(text="End Test", command=end_test)


# Place components in window
text_label.grid(row=0, column=0, columnspan=2)
start_btn.grid(row=2, column=0)
end_btn.grid(row=2, column=1)


if __name__ == "__main__":
    win.mainloop()
