from turtle import *
from random import *

pencil = Turtle()

for i in range(10):
    radius = randint(-200, 200)
    x = randint(-200, 200)
    y = randint(-200, 200)

    pencil.up()
    pencil.goto(x, y)
    pencil.down()

    pencil.circle(radius)