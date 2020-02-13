from tkinter import *
from functools import partial     # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting Variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(padx=100, pady=100, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (Row 0)
        self.converter_label = Label(self.converter_frame, text="Temperature", bg="light blue",
                                 font=("Arial","16", "bold"),
                                 padx=50, pady=50)
        self.converter_label.grid(row=0)

        # Help Button (Row 1)50
        self.help_buton = Button(self.converter_frame, text="help",
                                 padx=10, pady=10, command=self.help)
        self.help_buton.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __int__(self, partner):

        background = "orange"

        # Disable Help Button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (i.e: Help Box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (Row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions", bg=background,
                                 font=("Arial", "14", "bold"),
                                 padx=50, pady=50)
        self.how_heading.grid(row=0)

        # Help text (label, Row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss Button (Row 2)
        self.dismiss_btn = Button(self.help_frame, text= "Dismiss", width=10, bg=background,
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):

        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    start_program = Converter()
    root.mainloop()