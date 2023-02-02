import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

tess = turtle.Turtle()
draw_poly(tess, 8, 50)
turtle.done()
