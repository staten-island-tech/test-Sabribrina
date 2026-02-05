""" for i in range(3):
    print(i) """
import turtle
from turtle import *
t = Turtle()

""" for i in range(4):
    t.forward(100)
    t.left(90)

for i in range(3):
    t.forward(100)
    t.left(120) """

""" for i in range(60):
    def square(x):
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(5)
    square(200) """

""" sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90) """

""" def square(x):
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length)
        length = length * 2
doubleSquares(5) """

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length)
        length += 25
addSquares(5) """

""" def addSquares(iRange):
    length = 5
    for i in range(iRange):
        def square(x):
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
            t.forward(x)
            t.left(90)
            t.left(5)
        square(length)
        length += 5
addSquares(60) """

def addStars(iRange):
    length = 5
    for i in range(iRange):
        def Star(x):
            t.forward(x)
            t.left(144)
            t.forward(x)
            t.left(144)
            t.forward(x)
            t.left(144)
            t.forward(x)
            t.left(144)
            t.forward(x)
            t.left(144)
            t.left(5)
        Star(length)
        length += 5
addStars(60)

turtle.done()