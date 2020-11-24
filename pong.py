import turtle

# create a window
wn = turtle.Screen()
wn.title("Pong by Ellie")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops the window from updating
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle() # this is a turtle object
paddle_a.speed(0) # speed of animation, set to highest possible
paddle_a.shape("square") # choosing from one of the built in shapes
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # this will stretch the width of the paddle
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0) # choosing the starting position


# Paddle B
paddle_b = turtle.Turtle() # this is a turtle object
paddle_b.speed(0) # speed of animation, set to highest possible
paddle_b.shape("square") # choosing from one of the built in shapes
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # this will stretch the width of the paddle
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0) # choosing the starting position


# Ball
ball = turtle.Turtle() # this is a turtle object
ball.speed(0) # speed of animation, set to highest possible
ball.shape("square") # choosing from one of the built in shapes
ball.color("white")
ball.penup()
ball.goto(0, 0) # choosing the starting position
ball.dx = 2  # making the ball move - each time it moves it's by 2 pixels
ball.dy = 2 # this makes it move up and diagonally


# Function (to move the paddles)
def paddle_a_up():
    y = paddle_a.ycor() #.ycor method is from turtle, returns the y coordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor() #.ycor method is from turtle, returns the y coordinate
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() # .ycor method is from turtle, returns the y coordinate
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor() # .ycor method is from turtle, returns the y coordinate
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen() # sets the event listener
wn.onkeypress(paddle_a_up, "w") # the window will listen for the w key and call the paddle_a_up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") # listening for up and down arrow keys
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    #  move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (so ball doesn't fly off the screen)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this will reverse the direction if the ball hits the top

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # this will reverse the direction if the ball hits the top

    if ball.xcor() > 390:
        ball.goto(0, 0) # put ball back to center
        ball.dx *= -1 # reverse direction

    if ball.xcor() < -390:
        ball.goto(0, 0) # put ball back to center
        ball.dx *= -1 # reverse

     