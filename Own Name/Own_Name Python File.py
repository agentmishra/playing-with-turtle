#initializing
import turtle
an=turtle.Screen()
a=turtle.Turtle()

#setting up pen and page
an.bgcolor("yellow")
a.color("blue")
a.shape("circle")
a.pensize(10)

#moving pen left to start
a.penup()
a.left(360)
a.bk(260)
a.pendown()

#wriring: F
a.right(90)
a.fd(150)
a.bk(150)
a.left(90)
a.fd(80)
a.bk(80)
a.right(90)
a.fd(70)
a.left(90)
a.fd(50)
a.bk(50)
a.right(90)
a.fd(80)

#Using Space
a.penup()
a.left(90)
a.fd(50)
a.pendown()

#wriring: A
a.right(106)
a.bk(155)
a.left(30)
a.fd(155)
a.bk(60)
a.right(106)
a.fd(45)
a.bk(45)
a.left(106)
a.fd(60)

#Using Space
a.penup()
a.left(75)
a.fd(25)
a.pendown()

#wriring: R
a.right(90)
a.bk(150)
a.right(270)
a.circle(-35,140)
a.fd(25)
a.left(96)
a.fd(100)

#Using Space
a.penup()
a.left(45)
a.fd(30)
a.left(90)

#wriring: D
a.pendown()
a.right(90)
a.circle(80,180)
a.left(90)
a.fd(160)

#Using Space
a.penup()
a.left(90)
a.fd(120)
a.pendown()

#wriring: I
a.fd(15)
a.left(90)
a.fd(150)
a.right(90)
a.fd(15)
a.bk(30)
a.fd(15)
a.right(90)
a.fd(150)
a.right(90)
a.bk(15)

#Using Space
a.penup()
a.bk(30)
a.pendown()

#wriring: N
a.left(90)
a.bk(150)
a.left(30)
a.fd(170)
a.right(30)
a.bk(150)
a.penup()

#moving the pen from drawing
a.left(90)
a.fd(500)

#Holding the page to see
for x in range(180):
    a.left(12)