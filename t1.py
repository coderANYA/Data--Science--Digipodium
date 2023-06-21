from turtle  import *

speed('slowest')

#to  generate  a decagon

distance = 100
sides = 10

for i in range(sides):
    pencolor('red')
    fd(distance)
    rt(360/sides)
    circle(distance/2)
    for i in range(sides):           #nested loop
        pencolor('blue')
        fd(distance/2)
        rt(360/sides)
        dot(10)
        write(i)

hideturtle()
mainloop()