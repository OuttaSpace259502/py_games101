import tkinter as tk
from tkinter import Button, Message, font
from PIL import ImageTk as itk

# Coordinates for 2 buttons, side by side, from left to right
# Giving this button formation the color name 'red' to differenciate from other button groups
RED_Y_VALUE = 450
RED_LEFT_X_VALUE = 150
RED_RIGHT_X_VALUE = 560

# Coordinated for 3 buttons each stacked on top of each other
# This button group is called 'blue'
BLUE_X_VALUE = 550
BLUE_TOP_Y = 400
BLUE_MIDDLE_Y = 500
BLUE_BOTTOM_Y = 600


def welcome_page():
    # Generating screen text line by line
    message = "Welcome to the Memory Training Program"
    bold = "bold"
    header_line(message, bold)

    message = "This program will help you improve your memory and study for important exams. Would you like to enter your own material or receive a computer generated list to memorize?"
    screen_msg(message)

    # Generating buttons
    left_btn_msg = "Pc"
    right_btn_msg = "Input"
    red_buttons(left_btn_msg, right_btn_msg)


def all_pc_options():
    message = "Pick a category"
    screen_msg(message)

    top_msg = "Numbers"
    middle_msg = "Words"
    bottom_msg = "Mixed"
    blue_buttons(top_msg, middle_msg, bottom_msg)


def level_choice():
    message = "Depending on the level you pick, the amount of words to memorize will increase or decrease.\nPick a difficulty level."
    screen_msg(message)

    top_msg = "Easy"
    middle_msg = "Advanced"
    bottom_msg = "Pro"
    blue_buttons(top_msg, middle_msg, bottom_msg)


def personal_choice():
    # Generating screen text
    message = "There are 2 options to choose from. For the default version just enter the words of your choice. Vocabulary style will need a keyword followed by a value. The key/value pair will be displayed together."
    screen_msg(message)

    # Generating buttons
    left_btn_msg = "Default"
    right_btn_msg = "Vocabulary"
    red_buttons(left_btn_msg, right_btn_msg)


def interval_level():
    message = "The interval level will set the speed of the words appearing on the screen. Choose an interval level."
    screen_msg(message)

    top_msg = "Slow"
    middle_msg = "Medium"
    bottom_msg = "Fast"
    blue_buttons(top_msg, middle_msg, bottom_msg)


# def vocab_input():
#     message = 'Enter a keyword into the keyword entry box and a matching value into the value box. '


def enter_solution():
    message = "Enter everything the same order separated by a comma."
    screen_msg(message)


def madlibs_category():
    message = "Before you continue, we would like to help your memory with a mad libs. Please, choose a category:"
    screen_msg(message)

    top_msg = "Body"
    middle_msg = "Car"
    bottom_msg = "Home"
    blue_buttons(top_msg, middle_msg, bottom_msg)


def if_correct_end():
    message = "Congratulations!"
    bold = "bold"
    header_line(message, bold)

    message = "Your memory is impeccable! Would you like to play again?"
    screen_msg(message)

    left_btn_msg = "Quit"
    right_btn_msg = "Continue"
    red_buttons(left_btn_msg, right_btn_msg)


def ask_to_save():
    message = "Would you like to save your input list?"
    screen_msg(message)

    left_btn_msg = "No"
    right_btn_msg = "Yes"
    red_buttons(left_btn_msg, right_btn_msg)


# Generates all buttons and locates them according to x/y coordinated passed in.
def create_btn(button_text, x_value, y_value):
    btn = tk.Button(
        text=button_text,
        font=("RhodiumLibre-Regular", int(24.0)),
        bg="grey",
        activebackground="red",
    )
    btn.place(x=x_value, y=y_value, width=180, height=80)


def red_buttons(left_message, right_message):
    create_btn(left_message, RED_LEFT_X_VALUE, RED_Y_VALUE)
    create_btn(right_message, RED_RIGHT_X_VALUE, RED_Y_VALUE)


def blue_buttons(top_msg, middle_msg, bottom_msg):
    create_btn(top_msg, BLUE_X_VALUE, BLUE_TOP_Y)
    create_btn(middle_msg, BLUE_X_VALUE, BLUE_MIDDLE_Y)
    create_btn(bottom_msg, BLUE_X_VALUE, BLUE_BOTTOM_Y)


# def entry_box():
#     box = tk.(
#         bd=5,
#         relief='raised',
#         cursor='hand',

#     )


# This function makes the header bold wihtout effecting the rest of the body
def header_line(message, bold):
    screen_msg(message, bold)


# This function creates the lines and places them on the screen
def screen_msg(message, bold=""):
    screen_meesage = tk.Message(
        frame,
        text=message,
        justify="center",
        bg="#F4DF23",
        aspect=400,
        font=("RhodiumLibre-Regular", int(28.0), bold),
    )
    screen_meesage.pack(pady=10, padx=10)


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
    frame = tk.Frame(canvas, background="#F4DF23")
    frame.place(relx=0.25, rely=0.15, relwidth=0.8, relheight=0.4)
    madlibs_category()
    canvas.place(x=0, y=0)
    window.resizable(True, True)
    window.mainloop()
