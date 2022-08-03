import turtle

turtle.speed(10)

turtle.pencolor('green')
turtle.fillcolor('purple')

turtle.begin_fill()

# Draw a spiral 
for i in range(100):
    turtle.forward(i*3)
    turtle.left(60) # Changing the angle allows to create different spirals (90 creates a spiral of squares, 120 a triangular spiral, ...)
    
turtle.end_fill()

