from tkinter import *
from tkinter.messagebox import showinfo


def display_score(score):
    showinfo(title="Typing Speed Score", message=f"You type at {score} words per minute!")


win = Tk()
win.title = "Typing Speed"


if __name__ == "__main__":
    win.mainloop()
