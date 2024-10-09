import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
numside=10
sidelength=70
angle=360/numside
for i in range(numside):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()
