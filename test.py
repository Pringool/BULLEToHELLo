WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

import turtle

window = turtle.Screen()
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
#window.tracer(0)

t = turtle.Turtle()
t.speed(1)
#t.left(180)

while True:
    t.fd(1)
    print(t.xcor(), t.ycor())
    
    #window.update()