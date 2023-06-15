import turtle
from turtle import *

t = turtle.Turtle()
s = turtle.Screen()
s = bgcolor("black")
t.speed(70)
d = 0

for i in range(240):
    t.color("blue")
    t.circle(i)
    t.left(5)
    d += 1
    if d >= 500:
        break
        t.turtledone()