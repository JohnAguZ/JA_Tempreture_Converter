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
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                 text="To Centigrade", font="Arial 10 bold",
                                 bg="Khaki", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)
        # Answer Label (Row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 12 bold",
                                     fg="purple", bg=background_color, pady=10, padx=10)
        self.converted_label.grid(row=4)

        # History / Help Button frame (Row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


    

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    start_program = Converter()
    root.mainloop()