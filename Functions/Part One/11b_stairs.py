# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

import turtle

t = turtle.Turtle()
t.width(5)
t.color("green")

for n in range(7):
    t.forward(30)
    if n % 2 == 0:
        t.left(90)
    else:
        t.right(90)
