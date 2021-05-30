import turtle
import random

def triangle(length) :
    turtle.forward(length)
    turtle.left(200)
    turtle.forward(length)
    turtle.left(200)
    turtle.forward(length)
    turtle.left(200)

n=24

for i in range(n) :
    triangle(len/2)
    turtle.right(15)
    
turtle.hideturtle()     
