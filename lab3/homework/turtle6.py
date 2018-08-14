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

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    side_length = random.randint(3, 10)
    star('blue',x, y, side_length)
