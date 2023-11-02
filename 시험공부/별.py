import turtle

t = turtle.Pen()
colors = ['red', 'blue', 'yellow']

for x in range(500):
    t.pencolor(colors[x%3])
    t.forward(x)
    t.left(144)
