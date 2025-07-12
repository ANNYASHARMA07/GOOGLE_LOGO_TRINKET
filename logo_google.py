import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("white")
t.color("#4285F4") #blue
t.pensize(5)
t.speed(4)

t.fd(120)
t.rt(90)
t.circle(-150,50) 
t.color("green") #green
t.circle(-150,100)
t.color("#F4B400") #yellow
t.circle(-150,60)
t.color("red") #red

t.begin_fill()
t.circle(-150,100)
t.rt(90)
t.fd(50)
t.right(90)
t.circle(100,100)
t.rt(90)
t.fd(50)
t.end_fill()  #filing red color

t.begin_fill()
t.color("#F4B400")#yellow
t.rt(180)
t.fd(50)
t.right(90)

t.circle(100,60)
t.rt(90)
t.fd(50)
t.right(90)
t.circle(-150,60)
t.end_fill()

t.rt(90)
t.fd(50)
t.rt(90)
t.circle(100,60)
t.color("green")
t.begin_fill()
t.circle(100,100)
t.rt(90)
t.fd(50)
t.rt(90)
t.circle(-150,100)
t.rt(90)
t.fd(50)
t.end_fill()

t.rt(90)
t.circle(100,100)
t.color("#4285F4")  #blue
t.begin_fill()
t.circle(100,25)
t.lt(115)
t.fd(65)
t.rt(90)
t.fd(42)
t.rt(90)
t.fd(124)
t.rt(90)
t.circle(-150,50)
t.rt(90)
t.fd(50)
t.end_fill()

t.hideturtle()