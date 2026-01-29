import turtle
from turtle import *
t = Turtle()

""" t.forward(200) """


def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def rectangle():
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle()

def equal():
    t.forward(90)
    t.left(60)
    t.forward(90)
    t.left(60)
    t.forward(90)
equal()

turtle.done()