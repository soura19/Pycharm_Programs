import turtle
def square(length):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    return length * length
len=int(input("Enter Length: "))
area=square(len)
print("Area :", area)
