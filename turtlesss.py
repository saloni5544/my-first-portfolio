from turtle import *
import math


sides = int(input(' How many sides do you want in your house base? '))

# Name your Turtle.
t = Turtle()


# Set Up your screen and starting position.
setup(0,0)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
t.pendown()
t.speed (3)

for side in range (0,sides):
    t.forward(80)
    t.right(360/sides)
t.penup()



t.pendown()
t.pencolor("deepPink1")
t.right(60)
t.forward(50)
t.right(60)
t.forward(50)
t.right(-60)
t.forward(50)





# Close window on click.
exitonclick()
