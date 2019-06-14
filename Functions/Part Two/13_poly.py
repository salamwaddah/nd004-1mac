import turtle


def polygon(sides, length):
    t = turtle.Turtle()
    t.color("lime")
    t.speed(0)
    angle = 360 / sides
    for side in range(sides):
        t.forward(length)
        t.right(angle)
    t.hideturtle()


for side in range(3, 15):
    polygon(side, 35)
