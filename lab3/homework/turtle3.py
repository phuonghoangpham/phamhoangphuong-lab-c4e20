from turtle import *
shape('turtle')
color('red')
def draw_square(length, color):
    for i in range(4):
        forward(length)
        left(90)

# draw_square(50, color)       # Call the function to draw the square
# mainloop()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()