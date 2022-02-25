import turtle

t=turtle.Turtle()
t.penup()
t.goto(100,160)
t.pendown()

t.color("black" , "yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()

t.penup()
t.goto(50,100)
t.pendown()
t.left(100)
t.color("black" , "yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()

t.penup()
t.goto(-260,270)
t.pendown()
t.left(200)
t.color("black" , "yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()

