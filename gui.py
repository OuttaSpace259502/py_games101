import tkinter as tk
from tkinter import Button, Message, font
from tkinter.scrolledtext import ScrolledText
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

# Coordinates for small button (Submit, Quit, Answer)
SMALL_BTN_YVALUE = 650
SUBMIT_X_VALUE = 600
QUIT_X_VALUE = 1100
ANSWER_X_VALUE = 100
# Small button width and height
SB_WIDTH = 80
SB_HEIGHT = 20


def welcome_page():
    # Generating header and makes it bold
    message = "Welcome to the Memory Training Program"
    bold = "bold"
    header_line(message, bold)
    # Body text (not bold)
    message = "This program will help you improve your memory and study for important exams. Would you like to enter your own material or receive a computer generated list to memorize?"
    screen_msg(message)

    # Generating buttons (button formation group left to right => called red)
    left_btn_text = "Pc"
    right_btn_text = "Input"
    red_buttons(left_btn_text, right_btn_text)


def all_pc_options():
    message = "Pick a category"
    screen_msg(message)

    # Generating 3 buttons stacked on top of each other => this formation is called 'blue'
    top_text = "Numbers"
    middle_text = "Words"
    bottom_text = "Mixed"
    blue_buttons(top_text, middle_text, bottom_text)


def level_choice():
    message = "Depending on the level you pick, the amount of words to memorize will increase or decrease.\nPick a difficulty level."
    screen_msg(message)

    top_text = "Easy"
    middle_text = "Advanced"
    bottom_text = "Pro"
    blue_buttons(top_text, middle_text, bottom_text)


def personal_choice():
    # Generating screen text
    message = "There are 2 options to choose from. For the default version just enter the words of your choice. Vocabulary style will need a keyword followed by a value. The key/value pair will be displayed together."
    screen_msg(message)

    # Generating buttons
    left_btn_text = "Default"
    right_btn_text = "Vocabulary"
    red_buttons(left_btn_text, right_btn_text)


def interval_level():
    message = "The interval level will set the speed of the words appearing on the screen. Choose an interval level."
    screen_msg(message)

    top_text = "Slow"
    middle_text = "Medium"
    bottom_text = "Fast"
    blue_buttons(top_text, middle_text, bottom_text)


def default_input():
    message = "Enter each word followed by a comma."
    screen_msg(message)

    entry_box()

    btn_text = "Submit"
    create_small_button(btn_text)


# def vocab_input():
#     message = 'Enter a keyword into the keyword entry box and a matching value into the value box. '


def enter_solution():
    message = "Enter everything the same order separated by a comma."
    screen_msg(message)

    entry_box()

    btn_text = "Submit"
    create_small_button(btn_text)


def madlibs_category():
    message = "Before you continue, we would like to help your memory with a mad libs. Please, choose a category:"
    screen_msg(message)

    top_text = "Body"
    middle_text = "Car"
    bottom_text = "Home"
    blue_buttons(top_text, middle_text, bottom_text)


def madlibs_verbs():
    message = "Enter grotesque, crazy, over the top and easy to remember and visualize verbs into the entry box."
    screen_msg(message)

    entry_box()

    btn_text = "Submit"
    create_small_button(btn_text)


def if_correct_end():
    message = "Congratulations!"
    bold = "bold"
    header_line(message, bold)

    message = "Your memory is impeccable! Would you like to play again?"
    screen_msg(message)

    left_btn_text = "Quit"
    right_btn_text = "Continue"
    red_buttons(left_btn_text, right_btn_text)


def ask_to_save():
    message = "Would you like to save your input list?"
    screen_msg(message)

    left_btn_text = "No"
    right_btn_text = "Yes"
    red_buttons(left_btn_text, right_btn_text)


# Generates all buttons and locates them according to x/y coordinated passed in.
# Button size is also customizeable but is by default large
def create_btn(button_text, x_value, y_value, width=180, height=80):
    btn = tk.Button(
        text=button_text,
        font=("RhodiumLibre-Regular", int(24.0)),
        background="grey",
        activebackground="red",
    )
    btn.place(x=x_value, y=y_value, width=width, height=height)


# Creates 2 buttons lined up from left to right (Red = name of button placement)
def red_buttons(left_button_text, right_button_text):
    create_btn(left_button_text, RED_LEFT_X_VALUE, RED_Y_VALUE)
    create_btn(right_button_text, RED_RIGHT_X_VALUE, RED_Y_VALUE)


# Creates 3 buttons stacked on top of each other (Blue = name of button placement)
def blue_buttons(top_text, middle_text, bottom_text):
    create_btn(top_text, BLUE_X_VALUE, BLUE_TOP_Y)
    create_btn(middle_text, BLUE_X_VALUE, BLUE_MIDDLE_Y)
    create_btn(bottom_text, BLUE_X_VALUE, BLUE_BOTTOM_Y)


# Creates small buttons (Submit, Quit). By default centered.
def create_small_button(button_text, x_value=SUBMIT_X_VALUE, y_value=SMALL_BTN_YVALUE):
    width = SB_WIDTH
    height = SB_HEIGHT
    create_btn(button_text, x_value, y_value, width, height)


# Creates large entry box for user input
def entry_box():
    box = tk.Text(
        entry_frame,
        bd=5,
        relief="raised",
        cursor="hand",
    )
    box.pack(padx=10, pady=10)


# This function makes the header bold wihtout effecting the rest of the body
def header_line(message, bold):
    screen_msg(message, bold)


# This function creates the text lines which are displayed to users
# and places them on the screen. (Instructions etc.)
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
    canvas.place(x=0, y=0)

    frame = tk.Frame(canvas, background="#F4DF23")
    frame.place(relx=0.25, rely=0.15, relwidth=0.8, relheight=0.4)

    entry_frame = tk.Frame(canvas, background="#F4DF23")
    entry_frame.place(relx=0.4, rely=0.6, relwidth=0.6, relheight=0.3)
    default_input()
    window.resizable(True, True)
    window.mainloop()
