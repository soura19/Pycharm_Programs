import turtle
def triangle(side):
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    return side+side+side
len=int(input("enter length "))
perimeter=triangle(len)
print("perimeter=",perimeter)


    
    
    
