from turtle import*


pencil = Turtle()


def square(t, size, color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()



def circle(c, radius, color):
    c.color(color)
    c.begin_fill()
    c.circle(radius)
    c.end_fill()

def pentagon(p, size, color):
    p.color(color)
    p.begin_fill()
    for i in range(5):
        p.forward(size)
        p.left(72)
    p.end_fill()



start = input("square/circle/pentagon/stop\n").lower()

while start != "stop":
    start = input("square/circle/pentagon/stop\n").lower()
    if start == "square":
        square(pencil, 100, "red")
    elif start == "circle":
        circle(pencil, 60, "green")
    elif start == "pentagon":
        pentagon(pencil, 100, "blue")
    else:
        break


done()