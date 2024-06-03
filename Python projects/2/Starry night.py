import turtle as t
from random import randint, random

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

#main code
t.speed('fastest')
t.hideturtle()
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow' ,0, 0)

while True:
    ranPts = randint(2, 5)
    ranSize = randint(10, 50)
    ranCol =(random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)

    draw_star(ranPts, ranSize, ranCol, ranX, ranY)