import turtle

# Set the number of sides here.
sides = 100

# Set the length of a side here.
length = 2

t = turtle.Turtle()
t.color("orange")
t.speed(0)
for side in range(sides):
    t.forward(length)
    t.right(365 / sides)
    # On the line above, replace the
    # value 72 with an arithmetic
    # expression that uses the
    # 'sides' variable.
