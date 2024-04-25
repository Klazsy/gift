import turtle

def draw_heart():
    turtle.speed(2)
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(180)
    turtle.end_fill()
    turtle.hideturtle()

def display_message():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.write("Happy Birthday Evania!", align="center", font=("Arial", 20, "normal"))

if __name__ == "__main__":  # Fix: Correcting the usage of `__name__`
    draw_heart()
    display_message()
    turtle.done()
