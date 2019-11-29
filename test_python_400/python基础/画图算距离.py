import turtle, math

x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

p = turtle.Pen()
p.penup()
p.goto(x1, y1)
p.pendown()

p.goto(x2, y2)
p.goto(x3, y3)
p.goto(x4, y4)

distance = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
p.write(distance)
input()