import turtle

def draw_star(t, star_size):
    for i in range(5):
        t.forward(star_size)
        t.right(144)

t = turtle.Turtle()
draw_star(t, 100)
turtle.done()
