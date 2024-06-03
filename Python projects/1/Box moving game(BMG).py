import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Box moving Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates for manual control

# Draw the grid (optional, for visual reference)
grid_turtle = turtle.Turtle()
grid_turtle.penup()
grid_turtle.speed(0)
grid_turtle.color("gray")
grid_size = 20
for x in range(-300, 320, grid_size):
    grid_turtle.goto(x, -300)
    grid_turtle.pendown()
    grid_turtle.goto(x, 300)
    grid_turtle.penup()
for y in range(-300, 320, grid_size):
    grid_turtle.goto(-300, y)
    grid_turtle.pendown()
    grid_turtle.goto(300, y)
    grid_turtle.penup()
grid_turtle.hideturtle()

# Player (robot) setup
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)

# Box setup
box = turtle.Turtle()
box.shape("square")
box.color("brown")
box.penup()
box.speed(0)
box.goto(0, 0)

# Goal setup
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()
goal.speed(0)
goal.goto(100, 100)

# Movement functions
def move_left():
    x = player.xcor()
    x -= grid_size
    if x < -290:
        x = -290
    player.setx(x)
    check_collision()

def move_right():
    x = player.xcor()
    x += grid_size
    if x > 290:
        x = 290
    player.setx(x)
    check_collision()

def move_up():
    y = player.ycor()
    y += grid_size
    if y > 290:
        y = 290
    player.sety(y)
    check_collision()

def move_down():
    y = player.ycor()
    y -= grid_size
    if y < -290:
        y = -290
    player.sety(y)
    check_collision()

# Check for collision with box and goal
def check_collision():
    if player.distance(box) < 20:
        move_box()
    if player.distance(goal) < 20:
        goal_reached()

# Move box if collided
def move_box():
    if player.xcor() < box.xcor():
        box.setx(box.xcor() + grid_size)
    elif player.xcor() > box.xcor():
        box.setx(box.xcor() - grid_size)
    elif player.ycor() < box.ycor():
        box.sety(box.ycor() + grid_size)
    elif player.ycor() > box.ycor():
        box.sety(box.ycor() - grid_size)

# Goal reached
def goal_reached():
    goal.color("yellow")
    screen.update()
    print("Goal reached!")

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# Main game loop
while True:
    screen.update()

# Close the window when clicked
screen.mainloop()
