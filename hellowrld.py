from turtle import *
right(90)
integer = 1
y = 1

for loop  in range(7):
    forward(100)
    for loop in range(60):
        left(3*y)
        forward(1)
    if y == 1:
        y = -1
    else:
        if y == -1:
            y = 1
   

    
    
        
exitonclick()