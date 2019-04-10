#!/usr/bin/env python3

import path
import math

print("r=20000")
print("e=1")

step = 6
distance = 155
increment = 4.0

turtle = path.Turtle(2000, 1500, increment=increment)
turtle.turn(math.pi)
while True:
    turtle.turn((math.pi/200)*-50)
    for _ in range(0, 250):
        turtle.forward(step)
        turtle.turn(math.pi/200)
    turtle.turn(math.pi)
    for _ in range(0, 250):
        turtle.forward(step)
        turtle.turn(math.pi/200)
    turtle.forward(distance * step)
    turtle.turn((math.pi/200)*100)
    turtle.forward(distance * step)
    turtle.turn((math.pi/200) * 50)
    turtle.turn(math.pi/60)
