import turtle

turtle.speed(100)
turtle.fillcolor('green')

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

def polygon(side_len, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(side_len)
        turtle.left(360/sides)
    turtle.end_fill()
    if side_len > 0:
        turtle.left(2)
        turtle.forward(8)
        polygon(side_len - 1, sides)
        
polygon(110, 5)

turtle.done()