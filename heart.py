#!/usr/bin/env python3

import path
import math

print("r=20000")
print("e=1")

while True:
    turtle = path.Turtle(3500, 1500)
    turtle.turn(math.pi)
    turtle.turn((math.pi/200)*-50)
    for _ in range(0, 250):
        turtle.forward(10)
        turtle.turn(math.pi/200)
    turtle.turn(math.pi)
    for _ in range(0, 250):
        turtle.forward(10)
        turtle.turn(math.pi/200)
    turtle.line_to(3500 - ((3500 - turtle.x) / 2), 2500)
    turtle.line_to(3500, 1500)
