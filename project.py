from turtle import *

speed(0)

setup( width = 1350, height =765, startx = None, starty = None)

colormode(255)

bgcolor(0, 0, 0)

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
        begin_fill()
        circle(radius)
        end_fill()

        
def drawText():
        penup()
        setposition(230, 300)
        setheading(0)
        pendown()
        color("White")
        write("Kenneth Alexander's Turtle Project", font=("Arial", 16, "bold"))

def draw_continents():
    turtle = Turtle()
    screen = Screen()
    screen.onscreenclick(turtle.goto)
    turtle.getscreen()._root.mainloop()
    color(178, 255, 102)

draw_sun(80, 50, 36, "orange",  "red")
draw_star(400, 90, 10, 36, "white", "white")
draw_star(4, 200, 10, 36, "white", "white")
draw_star(300, 30, 10, 36, "white", "white")
draw_star(160, -300, 10, 36, "white", "white")
draw_star(200, -200, 10, 36, "white", "white")
draw_star(350, -178, 10, 36, "white", "white")
draw_star(400, 40, 10, 36, "white", "white")
draw_star(20, 50, 10, 36, "white", "white")
draw_star(-284, 50, 10, 36, "white", "white")
drawCircle(-250, 200, "gray", "gray", 100)
drawCircle(-380, -370, "blue", "blue", 200)
drawText()
draw_continents()
done()

