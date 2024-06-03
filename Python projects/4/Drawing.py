import turtle

def draw_shapes():
    screen = turtle.Screen()
    screen.title("Simple Drawing App")
    screen.setup(width=600, height=600)
    pen = turtle.Turtle()

    print("Welcome to the Drawing App!")
    print("Use arrow keys to draw. Press 'q' to quit.")

    def move_forward():
        pen.forward(10)

    def move_backward():
        pen.backward(10)

    def turn_left():
        pen.left(90)

    def turn_right():
        pen.right(90)

    def quit_app():
        screen.bye()

    screen.listen()
    screen.onkey(move_forward, "Up")
    screen.onkey(move_backward, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(quit_app, "q")

    turtle.done()

# Start drawing
draw_shapes()
