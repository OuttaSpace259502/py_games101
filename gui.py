import tkinter as tk
from tkinter import Button, font
from PIL import ImageTk as itk

# Coordinates for 2 buttons, side by side, from left to right
# Giving this button formation the color name red to differenciate from other button groups
RED_Y_VALUE = 450
RED_LEFT_X_VALUE = 150
RED_RIGHT_X_VALUE = 560

# Heading Line (bold)
header_y = 150

# Default coordinates for screen message who are one-liners (single line)
default_x = 445  # x-coordinate always stays the same no matter how many lines
default_middle_y = 250  # called default/middle line because all one liners will be using this y-cord. It is also the middle line y-cord for multiple line msgs.

# 2nd line (after one liner)
bottom_y = 300


def welcome_page():
    # Generating screen text line by line
    message = "Welcome to the Memory Training Program"
    bold = "bold"
    heading_line(message, bold)

    message = "This program will help you improve your memory and study"
    default_middle_line(message)

    message = "for important exams. Would you like to enter your own material "
    bottom_line(message)

    message = "or receive a computer generated list to memorize?"
    screen_msg(message, default_x, 350)

    # Generating buttons
    left_btn_msg = "Pc"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)
    right_btn_msg = "Input"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)


def all_pc_options():
    left_btn_msg = "Default"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    message = "There are 2 options to choose from. For the default version just"
    heading_line(message)

    message = "enter the words of your choice. Vocabulary style will need a keyword"
    default_middle_line(message)

    message = "followed by a value. The key/value pair will be displayed together."
    bottom_line(message)


def personal_choice():
    # Generating screen text
    message = "There are 2 options to choose from. For the default version just"
    screen_msg(message, default_x, 200)

    message = "enter the words of your choice. Vocabulary style will need a keyword"
    default_middle_line(message)

    message = "followed by a value. The key/value pair will be displayed together."
    bottom_line(message)

    # Generating buttons
    left_btn_msg = "Default"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)
    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)


def if_correct_end():
    message = "Congratulations!"
    bold = "bold"
    heading_line(message, bold)

    message = "Your memory is impeccable! Would you like to play again?"
    default_middle_line(message)

    left_btn_msg = "Quit"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)
    right_btn_msg = "Continue"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)


def ask_to_save():
    message = "Would you like to save your input list?"
    default_middle_line(message)

    left_btn_msg = "No"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)
    right_btn_msg = "Yes"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)


# Generates all buttons and locates them according to x/y coordinated passed in.
def create_btn(button_text, x_value, y_value):
    btn = tk.Button(
        text=button_text,
        font=("RhodiumLibre-Regular", int(24.0)),
        bg="grey",
        activebackground="red",
    )
    btn.place(x=x_value, y=y_value, width=180, height=80)


# The following 3 function determine the location of line generated
# This function places the header
def heading_line(message, bold):
    screen_msg(message, default_x, header_y, bold)


# This is the default line. If only one line needed on the screen this function will be used to place the line
# If multiple lines are needed => it functions as the middle or 2nd line.
def default_middle_line(message):
    screen_msg(message, default_x, default_middle_y)


# This function places the bottom line
def bottom_line(message):
    screen_msg(message, default_x, bottom_y)


# This is actually creating the lines and place them on the screen
# with the help of the previous 3 helper functions
def screen_msg(message, x_value, y_value, bold=""):
    canvas.create_text(
        x_value,
        y_value,
        text=message,
        fill="#000000",
        font=("RhodiumLibre-Regular", int(28.0), bold),
    )


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("900x700")
    window.configure(bg="#F4DF23")
    canvas = tk.Canvas(
        window,
        bg="#F4DF23",
        height=700,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    personal_choice()
    canvas.place(x=0, y=0)
    window.resizable(True, True)
    window.mainloop()
