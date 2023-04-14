"""
Pong.py

This program demonstrates the simple game of pong.
I created a copy of the original game with the help of a YouTube video,
and then made the sounds I wanted the game to have through FL Studio 20.8.4

Requirements:
    - Python 3.x
    - turtle module
    - pygame module

Functions:
    pong_r/l_up / pong_r/l_down:
        This function moves the right or left pad up or down respectively.
    border_sound and pad_sound:
        This function plays the respective sound when the ball touches the border or the pad.

Author:
    Panagiotis Zermpinos

Version:
    1.0 (April 2023)
"""

import turtle  # For graphics
import pygame  # For the sound fx

pygame.mixer.init()

# Setting the screen
window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)  # So that the window does not refresh itself, speeding up the gameplay

# Right pong
pad_r = turtle.Turtle()  # turtle.Turtle is a class object of turtle
pad_r.speed(0)
pad_r.shape('square')
pad_r.shapesize(stretch_wid=5, stretch_len=1)
pad_r.color('red')
pad_r.penup()  # So that it does not draw a line
pad_r.goto(-350, 0)

# Left pong
pad_l = turtle.Turtle()  # turtle.Turtle is a class object of turtle
pad_l.speed(0)
pad_l.shape('square')
pad_l.shapesize(stretch_wid=5, stretch_len=1)
pad_l.color('green')
pad_l.penup()  # So that it does not draw a line
pad_l.goto(350, 0)

# Ball
ball = turtle.Turtle()  # turtle.Turtle is a class object of turtle
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()  # So that it does not draw a line
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write('Player A: 0 Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Score
score_Player_A = 0
score_Player_B = 0


def pad_r_up():
    y = pad_r.ycor()  # ycor returns the y coordinate
    y += 20
    pad_r.sety(y)


def pad_r_down():
    y = pad_r.ycor()  # ycor returns the y coordinate
    y -= 20
    pad_r.sety(y)


def pad_l_up():
    y = pad_l.ycor()  # ycor returns the y coordinate
    y += 20
    pad_l.sety(y)


def pad_l_down():
    y = pad_l.ycor()  # ycor returns the y coordinate
    y -= 20
    pad_l.sety(y)


def border_sound():
    pygame.mixer.Sound('border.mp3').play()


def pad_sound():
    pygame.mixer.Sound('pong.mp3').play()


# Bind movement to keyboard
window.listen()
window.onkeypress(pad_r_up, 'w')
window.onkeypress(pad_r_down, 's')
window.onkeypress(pad_l_up, 'Up')
window.onkeypress(pad_l_down, 'Down')

while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounces
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        border_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        border_sound()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_Player_A += 1
        scoreboard.clear()
        scoreboard.write(f'Player A: {score_Player_A} Player B: {score_Player_B}',
                         align='center', font=('Courier', 24, 'normal'))
        border_sound()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_Player_B += 1
        scoreboard.clear()
        scoreboard.write(f'Player A: {score_Player_A} Player B: {score_Player_B}',
                         align='center', font=('Courier', 24, 'normal'))
        border_sound()

    if (340 < ball.xcor() < 350) and (ball.ycor() < pad_l.ycor() + 50) \
            and (ball.ycor() > pad_l.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        pad_sound()

    if (-340 > ball.xcor() > -350) and (ball.ycor() < pad_r.ycor() + 50) \
            and (ball.ycor() > pad_r.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        pad_sound()
