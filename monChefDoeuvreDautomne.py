"""
monChefDoeuvreDautomne.py

(c) 2016 Eric Sund; Andy Zeng

This program uses the Python Turtle Graphics Module in an attempt to draw a truncated version of Picasso's "Deux Enfants Lisant" painting.
The drawing will only feature the shoulders up, as shown in this image:
http://www.lsa.umich.edu/UMICH/lsa/Home/LSA%20Today/2013/images/Picasso-1.jpg
"""

#import the modules

import turtle as t
from turtle import *
import math
from math import *

#define the functions

def drawShape(shapeType, size, fillColor, colorOfPen, positionx = None, positiony = None, angle = 120, direction = 'forward'):
    t.penup()
    if positionx != None and positiony != None:
        t.setpos(positionx, positiony)
    t.pendown()
    t.pencolor(colorOfPen)
    t.fillcolor(fillColor)
    t.begin_fill()
    if shapeType == 'circle':
        drawCircle(size)
    elif shapeType == 'rectangle':
        drawRectangle(size)
    elif shapeType == 'square':
        drawSquare(size)
    elif shapeType == 'parallelogram':
        drawParallelogram(size, angle)
    elif shapeType == 'curl':
        drawCurl(size, direction)
    t.end_fill()


def drawCircle(size, angle):
    t.circle(size, angle)

def drawSquare(size):
    for i in range(2):
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.right(90)

def drawParallelogram(size, angle):
    for i in range (2):
        t.forward(size)
        t.left(angle)
        t.forward(size)
        t.left(180 - angle)

def drawRectangle(x, y):
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(y)

def drawCurl(size, bend = 1, direction = -1):
    t.pencolor('black')
    for i in range(size):
        t.left(direction * sqrt(i))
        t.forward(bend)

def eyes(x,y,radius,size=2):
    pos(x,y)
    t.fillcolor('black')
    t.begin_fill()
    x = x - radius  # our chosen position is the top right edge
    for i in range(60):  #over 60 slices
        t.goto(x+radius*cos(i*pi/60), y - radius*sin(i*pi/60))
    for i in range(60):  #over 60 slices
        t.goto(x-radius*cos(i*pi/60), y - radius/size*sin(i*pi/60))
    t.end_fill()

def pos(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

def move(size):
    t.penup()
    t.forward(size)
    t.pendown()

def drawLine(length, direction = 0, color='black'):
    t.pencolor(color)
    t.left(direction)
    t.forward(length)

def drawParabola(size, direction = -1):
    for i in range(size):
        t.left(direction * i)
        t.forward(math.pow(i, 2))

def xpos():
    xpos = t.position()[0]
    return xpos

def ypos():
    ypos = t.position()[1]
    return ypos


#MAIN
t.bgcolor("#b27e1e")

#begin drawing the left girl - coded by Eric

t.speed(10)
t.shape("turtle")

#Prepare an area for colour fill at the end
pos(-25, 50)
t.pencolor("")  #outline the fill colour area
t.begin_fill()
drawSquare(200)
t.fillcolor("#ceefee")
t.end_fill()

#shoulder in the left corner
t.pensize(5)
pos(-350, -350)
t.begin_fill()
drawLine(100, 45)
drawLine(30, -60)
drawLine(89, -120)
drawLine(37, -45)
t.color('gray')
t.end_fill()

#draw the hand of the right girl on the left side
pos(-250, -288)
t.begin_fill()
drawLine(50, -150)
drawLine(70, -80, "")
drawLine(52, -90)
drawLine(112, -40)
t.fillcolor('#698066')
t.end_fill()

#draw the the neck of the left girl on the bottom
t.right(175)
pos(-205, -350)
t.begin_fill()
drawLine(70, -5)
drawLine(110, 20)
drawLine(45, 90)
drawLine(125, 92)
drawLine(50, 18)
t.fillcolor('#40E0D0')
t.end_fill()
t.left(320)
pos(-20, 47)
t.pencolor('black')
t.begin_fill()
t.right(39.5)
t.circle(250, 70)
drawCurl(20, 5, +1)
drawCurl(15, 20, +1)
t.fillcolor('#c289d3')
t.end_fill()

#draw the head outline, and fill it at the end
pos(-140, -325)
t.left(236)
t.begin_fill()
drawCurl(15)
drawParabola(11)
t.left(-80)
drawCurl(10, 20)
t.circle(50, 50)
t.left(215)
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.right(90)
drawCurl(5, 1)
drawCurl(24, 11.7)
t.fillcolor('#40E0D0')
t.end_fill()
pos(-262, 35)
drawCurl(20, 3, +1)
drawCurl(15, 12, +1)
drawCurl(5, 23, +1)
drawLine(9)
pos(-22, 47)
drawLine(250, -40)
drawLine(50, -80)

#draw left eye
eyes(-120,-38.68, 45, 1.2)
t.right(74.5)

#begin oulining the same area again, to fill for lighter green!
t.pencolor("")
t.left(208)
pos(-140, -325)
t.left(236)
drawCurl(15)
drawParabola(11)
t.left(-80)
drawCurl(10, 20)
t.circle(50, 50)
t.left(215)
#fill from this spot right here
t.begin_fill()
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.right(90)
drawCurl(5, 1)
drawCurl(24, 11.7)
t.fillcolor("#ceefee")
t.end_fill()

#re-outline the nose due to filling that may overlap
pos(-22, 47)
drawLine(250, 60)
drawLine(50, -80)

#draw right eye
eyes(-10,-120,25,1.2)
t.right(100)

#fill colour under the nose
pos(-150, -183)
t.begin_fill()
#draw the outline to fill under the nose right here
drawLine(135, 205, "")
drawLine(130, 155, "")
drawLine(55, 100, "")
t.fillcolor("#ceefee")
t.end_fill()

#draw the mouth
t.pencolor('black')
pos(-165,-230)
t.right(185)
t.pensize(7)
drawParabola(6, +1)
pos(-155,-245)
t.right(7)
t.pensize(3)
drawParabola(5, +1)

#finish up the bottom designs for the neck
t.pensize(5)
pos(-170, -350)
t.begin_fill()
drawLine(160, -5)
drawLine(45, 120)
drawLine(110, 80)
t.fillcolor('#ceefee')
t.end_fill()
bottom_yval = ypos()

#hair strand
t.pensize(7)
pos(-362, -70)
t.right(120)
drawCurl(16, 8)

#draw and colour the fingers on the bottom
t.pensize(5)
pos(-275, -350)
drawLine(15, 90)
pos(-225, -350)
drawCurl(13, 2, +1)
pos(-210, -350)
t.left(-50)
t.begin_fill()
drawCurl(7, 7, +1)
t.right(155)
drawLine(52)
t.right(115)
drawLine(27)
t.fillcolor("#ce3737")
t.end_fill()
pos(-170, -320)
t.right(83)
drawLine(24)
t.circle(8, 180)
drawLine(24, 5)

#finish up drawing that last hair outline
pos(-277, -275)
drawLine(75, 100)

#draw the lines to connect the girl's ear and fill it
t.penup()
t.home()
pos(-23, 47)
t.begin_fill()
t.right(105)
drawParabola(8, +1)
drawCurl(25, 1, +1)
t.penup()
t.home()
pos(4, -108)
t.right(325)
drawCurl(21, 5, +1)
t.left(45)
drawLine(105, 0, "")
t.fillcolor('#40E0D0')
t.end_fill()

#end of the left girl


#begin drawing the right girl - coded by Andy

# Draw the right hair
t.penup()
t.home()
pos(115,145)            # Starting point
t.left(5)               ### ASSUMES THAT WE START ENTIRELY FACING RIGHT
t.begin_fill()
drawCurl(33, 15, -1)
t.goto(346.41,-190.00)  # End by shoulder
t.goto(215,-37)         # Close the shape
t.fillcolor('#723D39')
t.end_fill()
t.left(70)
pos(287.92,73.83)       # Start at right edge of face
drawCurl(16, 10, -1)    # Groove in her hair
t.goto(346.41,-190.00)  # End by shoulder

# Draw the left hair
pos(115,145)            # Starting point
t.right(150)
t.begin_fill()
drawCurl(20, 5, +1)     # Initial curve for hair
drawCurl(22, 3, +1)     # Tight turn
drawCurl(21, 7, +1)     # Smooth out the curve
t.goto(0,10)            # End at left edge of face
t.fillcolor('#723D39')
t.end_fill()

# Draw Head and neck
pos(0,10)
t.fillcolor('#698066')
t.begin_fill()
t.goto(173.21,-90.00)   # Using goto(x,y) for head because parallelogram is entirely assymetrical
t.goto(287.92,73.83)
t.goto(80,160)
t.goto(0,10)
t.end_fill()
pos(173.21,-90.00)      # Return to the chin in order to draw neck
t.left(24)
drawShape('parallelogram', 200, '#698066', 'black', angle = -130)   # Neck; may as well use the function
move(200)

# Draw right shoulder
t.fillcolor('#E1D849')
t.begin_fill()
drawCurl(18,5)          # End at same horizontal plane as parallelogram
rightshoulder_x = xpos()
t.goto(158.47,-258.40)  # Close shape at bottom of parallelogram
t.end_fill()

# Draw left shoulder
t.fillcolor('#E1D849')
t.begin_fill()
t.goto(40,-258.40)      # End near girl on the left
leftshoulder_x = xpos()
leftshoulder_y = ypos()
t.goto(-14.73,-158.40)  # End at left edge of parallelogram
t.end_fill()

# Draw the eyes
eyes(85,40,30,1.2)
eyes(255,80,30,1.2)

# Draw the Nose
pos(115,145)
t.goto(100,-15)
t.goto(140,0)

# Draw the Mouth
pos(135, -40)
t.goto(175, -30)

# Draw the signature box
t.penup()
t.home()
pos(leftshoulder_x,leftshoulder_y)
drawRectangle(rightshoulder_x - leftshoulder_x, leftshoulder_y -bottom_yval)

# Sign signatures in the box
bottom_of_letter = bottom_yval + 15
pos(leftshoulder_x + 60, bottom_of_letter)

# A is for Andy
t.pencolor("red")
t.right(20)
t.forward(35)
A1x = xpos()    #record position
A1y = ypos()
t.forward(35)
t.right(140)
top_of_letter = ypos()  #determine the top of letters
t.forward(35)
A2x = xpos()    #record position
t.forward(35)
t.penup()
t.home()        #return home, reset angle
t.pendown()
pos(A1x,A1y)
drawLine(A2x - A1x, 0, 'red')

# Z is for Zeng
pos(A2x + 30, top_of_letter)
drawLine(30, 0, 'red')
t.goto(A2x + 30, bottom_of_letter)
drawLine(30, 0, 'red')
end_of_z = xpos()

# E is for Eric
t.pencolor("blue")
pos(end_of_z + 80, bottom_of_letter)
t.goto(end_of_z + 80,top_of_letter)
t.forward(30)
pos(end_of_z + 80,(top_of_letter-bottom_of_letter)/2 + bottom_of_letter)
t.forward(30)
pos(end_of_z + 80,bottom_of_letter)
t.forward(30)
end_of_E = xpos()

# S is for Sund
pos(end_of_E + 40, top_of_letter)
t.right(180)
drawCircle((top_of_letter-bottom_of_letter)/4,180)
t.right(180)
drawCircle((top_of_letter-bottom_of_letter)/4,-190)


# Hide the turtle
ht()

# Display the work of art
done()
