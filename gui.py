import tkinter as tk
from tkinter import Button, font
from PIL import ImageTk as itk

# Coordinates for 2 buttons, side by side, from left to right
# Giving this button formation the color name red to differenciate from other button groups
RED_Y_VALUE = 450
RED_LEFT_X_VALUE = 150
RED_RIGHT_X_VALUE = 560

# Heading Line (bold)
header_y = 200

# Default coordinates for screen message who are one-liners (single line)
default_x = 445  # x-coordinate always stays the same no matter how many lines
default_middle_y = 250  # called default/middle line because all one liners will be using this y-cord. It is also the middle line y-cord for multiple line msgs.

# 2nd line (after one liner)
bottom_y = 300


def btn_clicked():
    print("Button Clicked")


def welcome_page():
    left_btn_msg = "Pc"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Input"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    canvas.create_text(
        461.5,
        100.0,
        text="Welcome to the Memory Training Program",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(28.0), "bold"),
    )
    canvas.create_text(
        457.5,
        192.5,
        text="This program will help you improve your memory and study",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )

    canvas.create_text(
        455.0,
        250.0,
        text="for important exams. Would you like to enter your own material ",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )
    canvas.create_text(
        463.5,
        310.0,
        text="or receive a computer generated list to memorize?",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )


def all_pc_options():
    left_btn_msg = "Default"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    canvas.create_text(
        457.5,
        162.5,
        text="There are 2 options to choose from. For the default version just",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )


def personal_choice():
    left_btn_msg = "Default"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    message = "There are 2 options to choose from. For the default version just"
    screen_msg(message, default_x, header_y)

    message = "enter the words of your choice. Vocabulary style will need a keyword"
    screen_msg(message, default_x, default_middle_y)

    message = "followed by a value. The key/value pair will be displayed together."
    screen_msg(message, default_x, bottom_y)


def if_correct_end():
    left_btn_msg = "Quit"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Continue"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    message = "Congratulations!"
    screen_msg(message, default_x, header_y)

    message = "Your memory is impeccable! Would you like to play again?"
    screen_msg(message, default_x, default_middle_y)


def ask_to_save():
    left_btn_msg = "No"
    create_btn(left_btn_msg, RED_LEFT_X_VALUE, RED_Y_VALUE)

    right_btn_msg = "Yes"
    create_btn(right_btn_msg, RED_RIGHT_X_VALUE, RED_Y_VALUE)

    message = "Would you like to save your input list?"
    screen_msg(message, default_x, default_middle_y)


def create_btn(button_text, x_value, RED_y_value):
    btn = tk.Button(
        text=button_text,
        font=("RhodiumLibre-Regular", int(24.0)),
        bg="grey",
        activebackground="red",
    )
    btn.place(x=x_value, y=RED_y_value, width=180, height=80)


def screen_msg(message, x_value, y_value):
    canvas.create_text(
        x_value,
        y_value,
        text=message,
        fill="#000000",
        font=("RhodiumLibre-Regular", int(28.0)),
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
    ask_to_save(canvas)
    canvas.place(x=0, y=0)
    window.resizable(True, True)
    window.mainloop()
