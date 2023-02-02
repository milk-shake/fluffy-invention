import turtle


t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()
t.speed(0)
t.color('white')

w = turtle.Screen()
w.bgcolor("black")
w.title("BROWN")


size = 250
squares = 100
angle = 90/squares


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
