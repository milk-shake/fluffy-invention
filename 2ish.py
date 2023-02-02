import turtle

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.pendown()

size = 20
distance = 10
squares = 5

def draw_square():
    for _ in range(4):
        t.forward(size)
        t.left(90)
 
for _ in range(squares):
    draw_square()
    t.penup()
    t.right(90)
    t.forward(distance)
    t.right(90)
    t.forward(distance)
    t.right(180)
    size += distance*2
    t.pendown()

turtle.done()