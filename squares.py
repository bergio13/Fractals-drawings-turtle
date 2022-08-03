import turtle

turtle.speed(1)

# Draw 2 squares
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)