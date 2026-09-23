import turtle
#import math
p = turtle.Turtle()

p.speed(0)
p.hideturtle()
turtle.bgcolor("black")
p.pensize(2)

colors = ["red","orange","yellow","green","cyan","blue","purple"]

n = 15
for i in range(n):
    angle = i*(360/n)
    length = 60 + i*3
    color = colors[i%7]
    p.pencolor(color)
    p.seth(angle)
    #p.forward(length)
    p.circle(length,120)
    p.dot(10,color)
    p.penup()
    p.goto(0,0)
    p.pendown()