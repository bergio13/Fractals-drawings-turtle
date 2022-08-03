import turtle
import random

turtle.speed(0)
turtle.pencolor('dark slate blue')

turtle.penup()
turtle.goto(0, -200)
turtle.left(90)
turtle.pendown()



def branch(branch_len, angle):
    sf = random.uniform(0.6, 0.9)
    turtle.pensize(branch_len/30)
    if branch_len < 8:
        return
    else:
        turtle.forward(branch_len)
        turtle.left(angle)
        branch(sf * branch_len, random.randint(25, 45))
        turtle.right(angle*2)
        branch(sf * branch_len, random.randint(25, 45))
        turtle.left(angle)
        turtle.backward(branch_len)

branch(120, 20)
turtle.done()
