import turtle
import os
import winsound as wav

WN = turtle.Screen()
WN.title('pong')
WN.bgcolor('black')
WN.setup(width=800, height=600)
WN.tracer

player1 = (int(3))
player2 = (int(3))
rallys = (int(0))

#rallyss
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(-10, 200)
pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal"))

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
ball.dx = 4
ball.dy = 0

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("gold")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player1 = {}  player 2 = {}".format(player1, player2), align="center", font=("Courier", 24, "normal"))

#paddle_a movment
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


#69 nice <====3
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#paddle b movment
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def start_game():
    ball.dy = 3
    ball.goto(0, 0)
    player1 == (int(3))
    player2 == (int(3))
    rallys == (int(0))

#binds
WN.listen()
WN.onkeypress(paddle_a_up, "w")
WN.onkeypress(paddle_a_down, "s")
WN.onkeypress(paddle_b_up, "o")
WN.onkeypress(paddle_b_down, "l")
WN.onkeypress(start_game, "space")

#main game
while True:
    WN.update()

#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#ball colistion
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        wav.PlaySound("bounce.wav", wav.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        wav.PlaySound("bounce.wav", wav.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 4
        ball.dx *= -1
        player2 -= 1
        wav.PlaySound("hit back.wav", wav.SND_ASYNC)
        pen.clear()
        pen.hideturtle()
        pen.write("player1 = {}  player 2 = {}".format(player1, player2), align="center", font=("Courier", 24, "normal"))
        pen2.clear
        rallys = 0
        pen2.hideturtle
        pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 4
        ball.dx *= -1
        player1 -= 1
        wav.PlaySound("hit back.wav", wav.SND_ASYNC)
        pen.clear()
        pen.hideturtle()
        pen.write("player1 = {}  player 2 = {}".format(player1, player2), align="center", font=("Courier", 24, "normal"))
        pen2.clear
        rallys = 0
        pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal"))
        pen2.hideturtle
        
    #paddle colision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        wav.PlaySound("bounce.wav", wav.SND_ASYNC)
        rallys += 1
        pen2.clear()
        pen2.hideturtle()
        pen2.color = ("white")
        pen2.goto(-10, 200)
        pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal")) 
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50) and abs(ball.dx) <= (int(11)):
        ball.setx(-340)
        ball.dx *= -1.1
        wav.PlaySound("bounce.wav", wav.SND_ASYNC)
        rallys += 1
        pen2.clear()
        pen2.hideturtle()
        pen2.color = ("white")
        pen2.goto(-10, 200)
        pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal")) 
    elif ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50) and abs(ball.dx) >= (int(11)):
        ball.setx(-340)
        ball.dx *= -1
        wav.PlaySound("bounce.wav", wav.SND_ASYNC) 
        rallys += 1
        pen2.clear()
        pen2.hideturtle()
        pen2.color = ("white")
        pen2.goto(-10, 200)
        pen2.write("{}".format(rallys), align="center", font=("Courier", 24, "normal")) 
    
    #endscreen
    if player1 == 0:
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("red")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, -20)
        pen.clear()
        pen.write("game over", align="center", font=("Courier", 100, "normal"))
        paddle_a.setx(9999999)
        paddle_b.setx(9999999)
        player2 -= 4
        player1 -= 1
        wav.PlaySound("game over.wav", wav.SND_ASYNC)
    
    if player2 == 0:
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("red")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, -20)
        pen.clear()
        pen.write("game over", align="center", font=("Courier", 100, "normal"))
        paddle_a.setx(9999999)
        paddle_b.setx(9999999)
        player2 -= 1
        player1 -= 4
        wav.PlaySound("game over.wav", wav.SND_ASYNC)