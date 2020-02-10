from tkinter import *
from functools import partial # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting Variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        self.hello_label = Label(text="hello")
        self.hello_label.grid(row=0)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Tempreture Converter")
    root.mainloop()