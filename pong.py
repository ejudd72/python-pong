import turtle
import os

# create a window
wn = turtle.Screen()
wn.title("Pong by Ellie")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops the window from updating
wn.tracer(0)


# Score
winning_score = 3
score_a = 0
score_b = 0
is_winner = False
winner = ""
is_playing = True

paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()
pen = turtle.Turtle()

def get_winner():
    global score_a
    global score_b
    global is_winner
    global is_playing

    if score_a >= winning_score:
        is_winner = True
        is_playing = False
        return "Player A"
    if score_b >= winning_score:
        is_winner = True
        is_playing = False
        return "Player B"


def score_string():
    return "Player A: " + str(score_a) + "  Player B:  " + str(score_b)


def start_game():
    # Paddle A
    global paddle_a
    global paddle_b
    global pen
    global ball

    paddle_a.speed(0) # speed of animation, set to highest possible
    paddle_a.shape("square") # choosing from one of the built in shapes
    paddle_a.shapesize(stretch_wid=5, stretch_len=1) # this will stretch the width of the paddle
    paddle_a.color("white")
    paddle_a.penup()
    paddle_a.goto(-350, 0) # choosing the starting position

    # Paddle B
    paddle_b.speed(0) # speed of animation, set to highest possible
    paddle_b.shape("square") # choosing from one of the built in shapes
    paddle_b.shapesize(stretch_wid=5, stretch_len=1) # this will stretch the width of the paddle
    paddle_b.color("white")
    paddle_b.penup()
    paddle_b.goto(350, 0) # choosing the starting position

    # Ball
    ball.speed(0) # speed of animation, set to highest possible
    ball.shape("square") # choosing from one of the built in shapes
    ball.color("white")
    ball.penup()
    ball.goto(0, 0) # choosing the starting position
    ball.dx = (score_a + score_b + 1) * 2  # making the ball move - each time it moves it's by 2 pixels
    ball.dy = (score_a + score_b + 1) * 2 # this makes it move up and diagonally

    # Pen
    pen.speed(0)
    pen.color("white")
    pen.penup() # if we didn't set this then we would see a line drawn when it moves
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(score_string(), align="center", font=("Courier", 24, "normal"))


start_game()
is_playing = True

# Winner Pen
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup() # if we didn't set this then we would see a line drawn when it moves
pen2.hideturtle()


# Function (to move the paddles)
def paddle_a_up():
    y = paddle_a.ycor()  # .ycor method is from turtle, returns the y coordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def reset_game():
    global score_a
    global score_b
    global is_playing
    global is_winner
    if is_winner:
        score_a = 0
        score_b = 0
        is_playing = True
        is_winner = False
        pen.clear()
        pen2.clear()
        start_game()


# keyboard binding
wn.listen()  # sets the event listener
wn.onkeypress(paddle_a_up, "w") # the window will listen for the w key and call the paddle_a_up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") # listening for up and down arrow keys
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    #  move the ball
    ball.setx((ball.xcor() + ball.dx))
    ball.sety((ball.ycor() + ball.dy))

    if is_winner:
        is_playing = False
        pen2.goto(0, 100)
        pen2.write(get_winner() + " Wins \n Press Enter to continue", align="center", font=("Courier", 30, "normal"))
        ball.dx = 0
        ball.dy = 0
        wn.onkeypress(reset_game, "Return")

        # Border checking (so ball doesn't fly off the screen)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this will reverse the direction if the ball hits the top
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # this will reverse the direction if the ball hits the top
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        score_a += 1
        get_winner()
        pen.clear()
        pen.write(score_string(), align="center", font=("Courier", 24, "normal"))

        ball.goto(0, 0) # put ball back to center
        ball.dx *= -1 # reverse direction

    if ball.xcor() < -390:
        score_b +=1
        get_winner()
        pen.clear()
        pen.write(score_string(), align="center", font=("Courier", 24, "normal"))

        ball.goto(0, 0) # put ball back to center
        ball.dx *= -1 # reverse

    # set up paddle collision
    # by comparing x and y coordinates of paddle and ball
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor() - 40):
        ball.setx(340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() < -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1