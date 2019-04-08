import this
from tkinter import *
from tkinter import messagebox

rot13 = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
)


def main_window(root):
    frame = Frame(root, width=100, height=100)
    zen_button = Button(root, text="Python Zen", command=show_zen)
    zen_button.pack()


def show_zen():
    messagebox.showinfo(
        "Zen of Python",
        this.s.translate(rot13)
    )


if __name__ == "__main__":
    root = Tk()
    main_window(root)
    root.mainloop()