import tkinter as tk
from tkinter import Button, font
from PIL import ImageTk as itk

Y_VALUE = 450
LEFT_X_VALUE = 150
RIGHT_X_VALUE = 560


def btn_clicked():
    print("Button Clicked")


def welcome_page(canvas):
    left_btn_msg = "Pc"
    create_btn(left_btn_msg, LEFT_X_VALUE, Y_VALUE)

    right_btn_msg = "Input"
    create_btn(right_btn_msg, RIGHT_X_VALUE, Y_VALUE)

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


def all_pc_options(canvas):
    left_btn_msg = "Default"
    create_btn(left_btn_msg, LEFT_X_VALUE, Y_VALUE)

    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RIGHT_X_VALUE, Y_VALUE)

    canvas.create_text(
        457.5,
        162.5,
        text="There are 2 options to choose from. For the default version just",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )


def personal_choice(canvas):
    left_btn_msg = "Default"
    create_btn(left_btn_msg, LEFT_X_VALUE, Y_VALUE)

    right_btn_msg = "Vocabulary"
    create_btn(right_btn_msg, RIGHT_X_VALUE, Y_VALUE)

    canvas.create_text(
        457.5,
        162.5,
        text="There are 2 options to choose from. For the default version just",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )

    canvas.create_text(
        455.0,
        220.0,
        text="enter the words of your choice. Vocabulary style will need a keyword ",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )
    canvas.create_text(
        463.5,
        280.0,
        text="followed by a value. The key/value pair will be displayed together.",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )


def if_correct_end(canvas):
    left_btn_msg = "Quit"
    create_btn(left_btn_msg, LEFT_X_VALUE, Y_VALUE)

    right_btn_msg = "Continue"
    create_btn(right_btn_msg, RIGHT_X_VALUE, Y_VALUE)

    canvas.create_text(
        461.5,
        115.5,
        text="Congratulations!",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(28.0), "bold"),
    )
    canvas.create_text(
        457.5,
        225.0,
        text="Your memory is impeccable! Would you like to play again?",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(24.0)),
    )


def ask_to_save(canvas):
    left_btn_msg = "No"
    create_btn(left_btn_msg, LEFT_X_VALUE, Y_VALUE)

    right_btn_msg = "Yes"
    create_btn(right_btn_msg, RIGHT_X_VALUE, Y_VALUE)

    canvas.create_text(
        445,
        179.0,
        text="Would you like to save your input list?",
        fill="#000000",
        font=("RhodiumLibre-Regular", int(28.0)),
    )


def create_btn(button_text, x_value, y_value):
    btn = tk.Button(
        text=button_text,
        font=("RhodiumLibre-Regular", int(24.0)),
        bg="grey",
        activebackground="red",
    )
    btn.place(x=x_value, y=y_value, width=180, height=80)


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
