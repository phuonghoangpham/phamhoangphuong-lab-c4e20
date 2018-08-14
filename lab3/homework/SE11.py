def is_inside():
    x_p=int(input("x coordinate of point: "))
    y_p=int(input("y coordinate of point: "))
    x_r=int(input("x coordinate of rectangle: "))
    y_r=int(input("y coordinate of rectangle: "))
    w=int(input("width of rectangle: "))
    h=int(input("height of rectangle: "))

    if x_r<=x_p<=x_r+w and y_r<=y_p<=y_r+h:
        print(True)
    else:
        print(False)

is_inside()