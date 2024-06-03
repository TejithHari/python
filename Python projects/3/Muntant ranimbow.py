import random
import turtle as t

#line length
def get_line_length():
    choice = input('Enter line length(long,medium,short): ')
    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    else:
        line_length = 100
        return line_length
    
#line width
def get_line_width():
    choice = input('Enter line width(superthick,thick,thin): ')
    if choice == 'superthick':
        line_width = 40
    elif choice == 'thick':
        line_width = 25
    else:
        line_width = 10
        return line_width
    
#inside window
def insidewindow():
    leftlimit = (-t.window_width() / 2) + 100
    rightlimit = (-t.window_width() / 2) - 100
    toplimit = (-t.window_height() / 2) - 100
    bottomlimit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = leftlimit < x < rightlimit and bottomlimit < y < toplimit
    return inside

#move the turtle
def moveturtle(line_length):
    pencolors =['red','orange','yellow','green','blue','purple']
    t.pencolor(random.choice(pencolors))
    if insidewindow():
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)
    
line_length = get_line_length()
line_width = get_line_width()

t.hideturtle()
t.fillcolor('red')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

while True:
    moveturtle(line_length)
