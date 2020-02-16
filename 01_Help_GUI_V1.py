from tkinter import *
from functools import partial     # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting Variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300,height=100, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.converter_label = Label(self.converter_frame, text="Temperature Converter", bg="light blue",
                                 font=("Arial","16", "bold"),
                                 padx=50, pady=50)
        self.converter_label.grid(row=0)

        # Help Button (Row 1)
        self.temp_instructions = Label(self.converter_frame,
                                       text="Type in the amount to be "
                                            "converted and then push "
                                            "one of the buttons below... ",
                                 font="Arial 10 italic", wrap=250,
                                 justify=LEFT, bg=background_color,
                                 padx=10, pady=10)
        self.temp_instructions.grid(row=1)

        # Temperature entry box (Row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons fram (Row 3), orchid3 | khakil

        # Answer Label (Row 4)

        # History / Help Button frame (Row 5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    start_program = Converter()
    root.mainloop()