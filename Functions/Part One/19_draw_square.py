import turtle

jack = turtle.Turtle()
jack.color("yellow")


def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)


draw_square()
