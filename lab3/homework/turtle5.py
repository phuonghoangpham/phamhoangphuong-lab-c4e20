import turtle
import random

def star(color, side_length, x, y):
    print(color, side_length, x, y)
    turtle.color(color)
    turtle.goto(x, y)
    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)
        turtle.forward(side_length)
star('green',100,0,0)

