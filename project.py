from turtle import *

bgcolor("black")

def draw_sun(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(200)
        left(turn)
    end_fill()

    
def draw_star(x, y, points, size, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(size)
        left(turn)
    end_fill()


def drawCircle(x, y, line, fill, radius):
        penup()
        setposition(x, y)
        pendown()
        color(line, fill)
        circle(radius)
        
        begin_fill()
        for i in range(y):
            forward(radius)
            left(turn)
        end_fill()

        
def drawText():
        penup()
        setposition(300, 300)
        setheading(0)
        pendown()
        color("White")
        write("Kenneth Alexander's Turtle Project", font=("Arial", 16, "bold"))


draw_sun(80, 50, 36, "orange",  "red")
draw_star(-200, 50, 10, 36, "white", "white")
draw_star(4, 200, 10, 36, "white", "white")
draw_star(0, 0, 10, 36, "white", "white")
draw_star(160, -300, 10, 36, "white", "white")
draw_star(-200, -200, 10, 36, "white", "white")
draw_star(-350, -178, 10, 36, "white", "white")
draw_star(400, 40, 10, 36, "white", "white")
draw_star(20, 50, 10, 36, "white", "white")
draw_star(-284, 50, 10, 36, "white", "white")

drawCircle(-250, 200, "gray", "gray", 100)
drawCircle(-300, -370, "blue", "blue", 300)
drawText()
done()

