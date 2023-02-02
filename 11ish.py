import turtle
import random


w = turtle.Screen()
w.bgcolor("black")
w.title("SUN")

star_colors = [(175, 201, 255),  (199, 216, 255),  (255, 244, 243),
               (255, 229, 207),  (255, 217, 178),  (255, 199, 142),  (255, 166, 81)]

t = turtle.Turtle()
t.penup()
t.goto(-w.window_width()/2, w.window_height()/2)
t.pendown()
t.speed(0)
turtle.colormode(255)


def draw_star(star_size):
    for _ in range(5):
        t.forward(star_size)
        t.right(144)


for i in range(200):
    draw_star(random.randint(2, 8))
    t.penup()
    t.color(star_colors[random.randint(0, len(star_colors)-1)])
    t.forward(w.window_width() - i - random.randint(0, 200))
    t.right(100 + random.randint(0, int(i/10)))
    t.pendown()


size = 100
squares = 100
angle = 90/squares
t.penup()
t.goto(0, 0)
t.pendown()
turtle.colormode(255)
t.color(253, 184, 19)


def draw_square():
    for _ in range(4):
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.right(90)


for _ in range(squares):
    draw_square()
    t.right(angle)

turtle.done()
