import turtle


t = turtle.Turtle()
t.speed(3)


t.color("orange")


t.begin_fill()


for _ in range(5):
    t.forward(150) 
    t.right(144)   


t.end_fill()


turtle.done()