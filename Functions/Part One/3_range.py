import turtle

t = turtle.Turtle()
t.color("magenta")
t.width(5)

for side in range(100):
    t.forward(5)
    t.right(360 / 100)
