import turtle


def spiral(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(turn)


spiral(50, 50, "blue", 2)
spiral(50, 51, "red", 2)
spiral(50, 51, "yellow", 2)
spiral(50, 52, "green", 2)
