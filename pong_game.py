# Simple Pong in Python 3 for Beginners
# Part 1: Getting Started


import turtle

window = turtle.Screen()
window.title("Gorgeous by @piiiinkeyey")
window.bgcolor("pink")
window.setup(width=800, height=600)
window.tracer(0)                    # Stops window from updating. Has to be updated manually which speeds up the game.


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # small 't' for module and 'T' for class name
paddle_a.speed(0)   # Animation speed, not paddle speed
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()  # small 't' for module and 'T' for class name
paddle_b.speed(0)   # Animation speed
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  # small 't' for module and 'T' for class name
ball.speed(0)   # Animation speed
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 3         # Everytime ball moves, it moves by 3 pixels
ball.dy = 3


# Pen
pen = turtle.Turtle()
pen.speed(0)        # Animation Speed
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gorgeous : 0   Steve Jobs : 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40             # Speed & direction of paddle
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


window.listen()         # Listen for keyboard input
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "d")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop

while True:
    window.update()     # Everytime Loop runs, it updates the screen
    # Moving ball
    ball.setx(ball.xcor() + ball.dx)  # .xcor/.ycor are current coordinates + dx/dy speed of ball (3 Pixels)
    ball.sety(ball.ycor() + ball.dy)

    # Boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1          #Reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Gorgeous : {}   Steve Jobs: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Gorgeous : {}   Steve Jobs: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

