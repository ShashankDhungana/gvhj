import turtle

wn=turtle.Screen()
pen=turtle.Turtle()
sides=3
length=200
angle=720//sides
for i in range(sides):
    pen.forward(length)
    pen.right(angle)
turtle.done()