import turtle
import os

size = 10
distance = size/2
squares = 50

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()
t.right(90)
t.forward(distance)
t.right(90)
t.speed(10)


def draw_square():
    for _ in range(2):
        t.forward(size)
        t.right(108)


for _ in range(squares):
    draw_square()
    size += distance

draw_square()
turtle.done()

