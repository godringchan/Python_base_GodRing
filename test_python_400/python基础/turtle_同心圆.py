import turtle
p = turtle.Pen()
pen_color = ("red", "blue", "yellow", "green", "black", "pink")
p.width(5)
p.speed(10)

for i in range(10):
    p.penup()
    p.goto(0, -i*10)
    p.pendown()
    p.color(pen_color[i % len(pen_color)])
    p.circle(10+i*10)


turtle.done()
