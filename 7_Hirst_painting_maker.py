import turtle
import random
import colorgram
from turtle import Screen


rbg_colors = []
colors = colorgram.extract('images.jfif', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rbg_colors.append(new_color)

new_color_list = []
for item in rbg_colors:
    new_color_list.append(item)

screen = Screen()
screen.bgcolor("black")

timmah = turtle
timmah.colormode(255)
timmah.speed('fastest')


def draw_art():
    for column in range(10):
        timmah.penup()
        timmah.setposition(-220, (-170 + (column * 40)))
        for row in range(10):
            timmah.pendown()
            timmah.dot(20, random.choice(new_color_list))
            timmah.penup()
            timmah.forward(50)

timmah.penup()
timmah.setposition(-220, -170)
draw_art()
timmah.hideturtle()


turtle.exitonclick()
