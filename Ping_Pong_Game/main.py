import turtle as t

# var
playerA = 1
playerB = 1

# window
window = t.Screen()
window.title('Ping Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# left paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color('white')
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# right paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color('white')
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(5, 5)
ball_x_direction = 0.2
ball_y_direction = 0.2

# scorecard
pen = t.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 3   Player B: 3 ", align='center', font=('Arial', 24, 'normal'))


# left paddle movement
def left_paddle_up():
    y = leftPaddle.ycor()
    y = y + 15
    leftPaddle.sety(y)


def left_paddle_down():
    y = leftPaddle.ycor()
    y = y - 15
    leftPaddle.sety(y)


# right paddle movement
def right_paddle_up():
    y = rightPaddle.ycor()
    y = y + 15
    rightPaddle.sety(y)


def right_paddle_down():
    y = rightPaddle.ycor()
    y = y - 15
    rightPaddle.sety(y)


# assign key for movement
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

while True:
    if(playerA > 0 or playerB >0):

        window.update()

        ball.setx(ball.xcor() + ball_x_direction)
        ball.sety(ball.ycor() + ball_y_direction)

        # border
        if ball.ycor() > 290:
            ball.sety(290)
            ball_y_direction = ball_y_direction * -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball_y_direction = ball_y_direction * -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_x_direction = ball_x_direction * -1
            playerA = playerA - 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(playerA, playerB), align='center',
                      font=('Arial', 24, 'normal'))
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_x_direction = ball_x_direction * -1
            playerB = playerB - 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(playerA, playerB), align='center',
                      font=('Arial', 24, 'normal'))

        # collisions
        if (ball.xcor() > 340) and (ball.xcor() < 350) and (
                ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40):
            ball.setx(340)
            ball_x_direction = ball_x_direction * -1

        if (ball.xcor() < -340) and (ball.xcor() > -350) and (
                ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40):
            ball.setx(-340)
            ball_x_direction = ball_x_direction * -1

    else:
        window.clearscreen()
        pen.write('game over', align='center', font=('Arial', 24, 'normal'))

