#This code was written by Elliott Hager, on 3/20/2020 for an Adv. Geomerty Olympics Project

#Import
import turtle
import math
import random

#Process
wn=turtle.Screen()
Penspeed=(10)

#Flag Outline
Flag_Outline=turtle.Turtle()
Flag_Outline.speed(Penspeed)
Flag_Outline.hideturtle()
Flag_Outline.pensize(4)
Flag_Outline.shape("circle")
Flag_Outline.penup()
Flag_Outline.goto(-225.27,150.315)
Flag_Outline.pendown()
for i in range(2):
  Flag_Outline.forward(450.0)
  Flag_Outline.right(90)
  Flag_Outline.forward(225)
  Flag_Outline.right(90)

#Olympic Stripes

#Blue
Olympic_Stripe_Blue=turtle.Turtle()
Olympic_Stripe_Blue.speed(Penspeed)
Olympic_Stripe_Blue.pencolor("#0085C7")
Olympic_Stripe_Blue.hideturtle()
Olympic_Stripe_Blue.penup()
Olympic_Stripe_Blue.goto(-112.77,150.315)
Olympic_Stripe_Blue.pendown()
Olympic_Stripe_Blue.right(90)
Olympic_Stripe_Blue.fillcolor('#0085C7')
Olympic_Stripe_Blue.begin_fill()
Olympic_Stripe_Blue.forward(222.2)
Olympic_Stripe_Blue.pencolor("#0085C7")
for i in range(1):
  Olympic_Stripe_Blue.right(90)
  Olympic_Stripe_Blue.forward(109.5)
  Olympic_Stripe_Blue.right(90)
  Olympic_Stripe_Blue.forward(222.2)
  Olympic_Stripe_Blue.right(90)
  Olympic_Stripe_Blue.forward(109.5)
Olympic_Stripe_Blue.end_fill()

#Yellow
Olympic_Stripe_Yellow=turtle.Turtle()
Olympic_Stripe_Yellow.speed(Penspeed)
Olympic_Stripe_Yellow.hideturtle()
Olympic_Stripe_Yellow.pencolor('#F4C300')
Olympic_Stripe_Yellow.fillcolor('#F4C300')
Olympic_Stripe_Yellow.penup()
Olympic_Stripe_Yellow.goto(-0.27,150.315)
Olympic_Stripe_Yellow.pendown()
Olympic_Stripe_Yellow.begin_fill()
for i in range(1):
  Olympic_Stripe_Yellow.right(90)
  Olympic_Stripe_Yellow.forward(223)
  Olympic_Stripe_Yellow.right(90)
  Olympic_Stripe_Yellow.forward(113.5)
  Olympic_Stripe_Yellow.right(90)
  Olympic_Stripe_Yellow.forward(223)
  Olympic_Stripe_Yellow.right(90)
  Olympic_Stripe_Yellow.forward(113.5)
Olympic_Stripe_Yellow.end_fill()

#Black
Olympic_Stripe_Black=turtle.Turtle()
Olympic_Stripe_Black.speed(Penspeed)
Olympic_Stripe_Black.hideturtle()
Olympic_Stripe_Black.pencolor('Black')
Olympic_Stripe_Black.fillcolor('Black')
Olympic_Stripe_Black.penup()
Olympic_Stripe_Black.goto(113.23,150.315)
Olympic_Stripe_Black.pendown()
Olympic_Stripe_Black.begin_fill()
for i in range(1):
  Olympic_Stripe_Black.right(90)
  Olympic_Stripe_Black.forward(223)
  Olympic_Stripe_Black.right(90)
  Olympic_Stripe_Black.forward(113.5)
  Olympic_Stripe_Black.right(90)
  Olympic_Stripe_Black.forward(223)
  Olympic_Stripe_Black.right(90)
  Olympic_Stripe_Black.forward(109.5)
Olympic_Stripe_Black.end_fill()

#Green
Olympic_Stripe_Green=turtle.Turtle()
Olympic_Stripe_Green.speed(Penspeed)
Olympic_Stripe_Green.hideturtle()
Olympic_Stripe_Green.pencolor('#009F3D')
Olympic_Stripe_Green.fillcolor('#009F3D')
Olympic_Stripe_Green.penup()
Olympic_Stripe_Green.goto(221.85,148.315)
Olympic_Stripe_Green.pendown()
Olympic_Stripe_Green.begin_fill()
for i in range(1):
  Olympic_Stripe_Green.right(90)
  Olympic_Stripe_Green.forward(220)
  Olympic_Stripe_Green.right(90)
  Olympic_Stripe_Green.forward(113.5)
  Olympic_Stripe_Green.right(90)
  Olympic_Stripe_Green.forward(220)
  Olympic_Stripe_Green.right(90)
  Olympic_Stripe_Green.forward(109.5)
Olympic_Stripe_Green.end_fill()

#Red Dot
Red_Dot=turtle.Turtle()
Red_Dot.speed(Penspeed)
Red_Dot.hideturtle()
Red_Dot.color("#DF0024")
Red_Dot.shape("circle")
Red_Dot.begin_fill()
Red_Dot.circle(45)
Red_Dot.end_fill()
Red_Dot.goto(0,22.5)

#Random Ange Cycle
Angel_of_Turn=random.choice([45,90,30,36,80,190])

#Lines
Lines_in_Circle=turtle.Turtle()
Lines_in_Circle.speed(Penspeed)
Lines_in_Circle.hideturtle()
Lines_in_Circle.penup()
Lines_in_Circle.goto(0,45)
Lines_in_Circle.pendown()
Lines_in_Circle.right(195)
for i in range (11):
  Lines_in_Circle.forward(45)
  Lines_in_Circle.goto(0,45)
  Lines_in_Circle.right(15)
Lines_in_Circle.penup()
Lines_in_Circle.goto(0,45)
Lines_in_Circle.pendown()
Lines_in_Circle.right(90)
Lines_in_Circle.forward(45)

#Tangent Lines
Tangent_Lines=turtle.Turtle()
Tangent_Lines.hideturtle()
Tangent_Lines.pensize(3)
Tangent_Lines.speed(Penspeed)
Tangent_Lines.pencolor("#DF0024")
Tangent_Lines.penup()
Tangent_Lines.goto(-45.75,150.315)
Tangent_Lines.pendown()
Tangent_Lines.right(90)
Tangent_Lines.forward(224)
Tangent_Lines.penup()
Tangent_Lines.goto(45.75,150.315)
Tangent_Lines.pendown()
Tangent_Lines.forward(224)


#Slogan
Slogan=turtle.Turtle()
Slogan.hideturtle()
Slogan.penup()
Slogan.goto(-225.27,-100)
Slogan.pendown()
Slogan.write("Let the best countries in the world compete!",False,font=("Arial", 17,"normal"))

