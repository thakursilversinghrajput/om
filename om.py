from turtle import Turtle,Screen
import turtle
import random
k=Turtle()
s=Screen()
s.bgcolor("black")
k.speed(0)


k.color("Red")
k.penup()
k.goto(-150,200)



k.circle(-25,-45)
k.pendown()
k.begin_fill()
k.circle(-100,90)
k.circle(-100,90)
k.right(80)
k.circle(100,-45)
k.circle(125,-70)
k.circle(150,-90)


k.seth(20)
k.fd(20)
k.right(70)
k.circle(125,90)
k.circle(100,90)
k.circle(25,90)
k.right(180)
k.fd(15)
k.circle(90,90)
k.circle(75,90)
k.right(35)

k.end_fill()

k.penup()
k.goto(-25,50)
k.pendown()
k.begin_fill()
k.left(60)
k.circle(50,-90)
k.circle(25,-45)
k.circle(50,-45)
k.back(45)
k.circle(-50,-45)
k.circle(-150,-45)
k.right(20)
k.circle(-150,45)
k.circle(-60,45)
k.circle(50,90)
k.circle(50,45)
k.circle(60,45)
k.fd(50)
k.end_fill()

k.penup()
k.goto(0,250)
k.right(40)
k.pendown()
k.begin_fill()
k.left(50)
k.circle(100,90)
k.circle(100,90)
k.left(90)

k.left(70)
k.circle(-100,90)
k.circle(-90,80)
k.left(172)
k.fd(45)
k.end_fill()

k.penup()
k.goto(50,205)
k.pendown()
k.begin_fill()
k.goto(40,170)
k.goto(75,160)
k.goto(85,195)
k.goto(50,205)
k.end_fill()
k.hideturtle()
k.pensize(7)
clrs=["violet","red","pink","blue","yellow"]
clrs2=["red","pink","violet","yellow","blue"]
for x in range(360):
    k.color(clrs[x%4])


k.penup()
k.goto(-210,270)
k.pendown()
k.circle(280,360)
k.color(clrs[x%4])
k.penup()
k.goto(-230,300)
k.pendown()
k.circle(320,360)
k.color(clrs[x%4])
k.penup()
k.goto(-250,330)
k.pendown()
k.circle(360,360)
k.color(clrs[x%4])
k.penup()
k.goto(-270,360)
k.pendown()
k.circle(400,360)
k.color(clrs[x%4])
k.penup()
k.goto(-290,390)
k.pendown()
k.circle(440,360)
k.color(clrs2[x%4])






turtle.done()





