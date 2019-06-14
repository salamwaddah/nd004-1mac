import turtle

salam = turtle.Turtle()
salam.width(5)
salam.speed(0)

rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# Write whatever code you want here!
for color in rainbow:
    salam.color(color)
    salam.forward(20)
    salam.right(20)
    salam.forward(30)
    salam.right(30)
