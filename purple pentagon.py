import turtle

color = "purple"
distance = 100
sides = [1, 2, 3, 4, 5]
angle = 72
mary = turtle.Turtle()
mary.color(color)

for side in sides:
    mary.forward(distance)
    mary.right(angle)
