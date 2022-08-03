import turtle

turtle.speed(100)
turtle.right(30)
turtle.shape('triangle')
turtle.penup()
turtle.ht()
turtle.pencolor('blue')
turtle.fillcolor('black')

def sierpinski(length, order):
    if order == 0:
        turtle.stamp()
    else:   
        for i in range(3):
            turtle.begin_fill()
            turtle.forward(length)
            sierpinski(length/2, order - 1)
            turtle.backward(length)
            turtle.left(120)
            turtle.end_fill()

sierpinski(150, 5)

turtle.done()