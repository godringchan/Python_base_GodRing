import turtle, random

a = random.randint(10, 36)
t = turtle.Pen()
for x in range(a):
    t.forward(x)
    t.left(30)

