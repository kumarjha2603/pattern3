import turtle as t
t.bgcolor("green")
a1=t.Turtle()
a1.speed(1000)
X=['dark blue','dark blue','dark blue','dark blue', 'dark green', 'dark green', 'dark green', 'dark green', 'yellow', 'yellow', 'yellow', 'yellow', 'black', 'black', 'black', 'black', 'dark red', 'dark red', 'dark red', 'dark red', 'dark red']
a=t.Turtle()
a.hideturtle()
a.speed(1000)
a.color("green")
a.left(-90)
a.forward(100)
a.left(-90)
a.forward(100)
a.left(90)
V1,V2=10,1
a.color("red")
for x in range(1,1000):
    
    a1.color(X[x%15])
    a1.forward(x)
    a1.left(90)
    a.forward(V1)
    a.left(90)
    a.forward(V2)
    a.left(90)
    a.forward(V1)
    a.left(-90)
    a.forward(V2)
    a.left(-90)
t.done()

