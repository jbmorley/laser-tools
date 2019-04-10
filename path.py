#!/usr/bin/env python3

import time
import math


def increment(a, b):
    if (a < b):
        return b - a
    else:
        return (a - b) * -1
        

class Turtle(object):

    def __init__(self, x=2000, y=2000, increment=6.0):
        self.x = x
        self.y = y
        self.angle = 0.0
        self.increment = increment

    def turn(self, angle):
        self.angle = self.angle + angle

    def line_to(self, x, y):
        step_x = increment(self.x, x)
        step_y = increment(self.y, y)
        distance = math.sqrt((step_x * step_x) + (step_y * step_y))
        steps = distance / self.increment
        step_x = step_x / steps
        step_y = step_y / steps
        for _ in range(0, int(steps)):
            self.x = self.x + step_x
            self.y = self.y + step_y
            print("s=%d,%d,4095,4095,1,1" % (self.x, self.y))
        self.x = x
        self.y = y

    def forward(self, distance):
        x = math.sin(self.angle) * distance
        y = math.cos(self.angle) * distance
        self.line_to(self.x + x, self.y + y)

