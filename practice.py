from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()


    angle = 180 - (360 / points)

    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(200)
        left(angle)
    end_fill()

bgcolor("black")
speed(0)

draw_star(0, 0, 36, "red", "blue")
draw_star(-100, -100, 35, "green", "purple")
draw_star(-50, -30, 40, "yellow", "green")
draw_star(30, 82, 90, "blue", "green")

done()

