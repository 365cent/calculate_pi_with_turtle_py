"""
References:
https://stackoverflow.com/questions/37472761/filling-rectangles-with-colors-in-python-using-turtle
https://www.blog.pythonlibrary.org/2012/08/06/python-using-turtles-for-drawing/
https://docs.python.org/3/library/turtle.html
https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/
"""
import random
import math
import time
import turtle

inside = 0
outside = 0
count = 0
iterations = 1000000
random.seed(int(round(time.time()*1000))) # INSERT CODE TO SEED THE RANDOM NUMBER GENERATOR HERE

# Draw filled rectangle with turtle
def rectangle(l, w):
    t.begin_fill()
    for i in range(2):
            t.right(90)
            t.forward(l)
            t.right(90)
            t.forward(w)
    t.end_fill()

# Initial status widget
def init():
    t.setposition(150, 150)
    t.left(90)
    t.fillcolor("#eee")
    t.setposition(150, 150)
    for i in range(3):
        rectangle(300, 50)
        t.backward(100)
    t.right(90)

# Display current status
def display():
    t.left(90)
    t.setposition(150, 150)
    t.fillcolor("#eee")
    t.pencolor("#" + time.strftime("%H%M%S")) # The color of time
    for i in range(3):
        rectangle(300, 50)
        move(150, -37.5)
        t.write(status[i], align="center", font=("Calibri", 16, "normal"))
        move(-150, -62.5)
    t.right(90)

# Move turtle to relative location
def move(x=None, y=None):
    t.setx(t.xcor() + x)
    t.sety(t.ycor() + y)

# Set up turtle
turtle.setup(1000, 600)
turtle.delay(0)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
# Print status widget
label = ["Total Number of points", "Points within circle", "Pi estimation"]
t.penup()
t.setposition(150, 150)
t.right(90)
for i in label:
    t.write(i, font=("Calibri", 12, "normal"))
    t.forward(100)
t.left(90)
init()
# Draw circle
t.setposition(-200, -200)
t.pendown()
t.circle(200)
t.penup()
# Draw square
t.forward(200)
t.pendown()
for i in range(4):
    t.left(90)
    t.forward(400)
t.penup()
# Reset turtle speed
#t.speed(6)

# Estimation start
for i in range(iterations):
    t.setposition(-400,-200)
    # select two random numbers between 0 and 1
    x = random.random()
    y = random.random()
    move(x * 400, y * 400)
    d = t.distance(-200,0) # calculate distance from origin
    # increment the appropriate counter
    if d > 200:
        t.dot("#0a84ff")
        outside += 1
    else:
        t.dot("#ff2d55")
        inside += 1
    count += 1
    pi = 4 * inside / count # calculate the value of Pi
    status = [count, inside, pi]
    display()
    print("Current status\> Total Number of points: {}, Points within circle: {}, Pi estimation: {}".format(count, inside, pi), end='\r') # Print current estimation status
turtle.done()
# Estimation End
Print("The final result after {} times estimation is {}".format(iterations, pi)) # print result
