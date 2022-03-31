import turtle
import turtle as tmnt
from turtle import Screen
import random

screen = Screen()
timmah = tmnt.Turtle()
turtle.colormode(255)


def forward():
    timmah.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmah.forward(10)


def backward():
    timmah.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmah.backward(10)


def turn_right():
    timmah.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmah.right(10)


def turn_left():
    timmah.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmah.left(10)


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=timmah.reset)


turtle.exitonclick()
