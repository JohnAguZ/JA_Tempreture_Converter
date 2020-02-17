from tkinter import *
from functools import partial     # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting Variables
        background_color = "light blue"

        # Converter Frames
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (Row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                            font="Arial 16 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User Instructions (Row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                        text="Type the amount to be "
                                             "converted and then push "
                                             "one of the buttons below... ",
                                        font="Arial 16 italic",
                                        justify=LEFT,
                                        bg=background_color,
                                        padx=10, pady=10)

        self.temp_instructions_label.grid(row=1)

        # Temperature Entry Box (Row 2)
        self.to_convert_entry = Entry(self.converter_frame,
                                        width=20,
                                        font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion Buttons Frame (Row 3), orchid3 | khakil
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="khaki1",padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1",padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer Label (Row 4)
        self.hist_help_frame = Frame(self.converter_frame)

        # History / Help Button (Row 5)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    start_program = Converter()
    root.mainloop()