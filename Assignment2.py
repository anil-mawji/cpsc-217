##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *
from math import *

WIDTH = 800
HEIGHT = 600
origin = {"x": WIDTH / 2, "y": HEIGHT / 2}

background("white")

# Draw x-axis
line(0, origin["y"], WIDTH, origin["y"])
for x in range(10, WIDTH, 30):
    # Draw horizontal tick
    line(x, origin["y"] - 3, x, origin["y"] + 3)
    label = x // 30 - 13
    if label != 0:
        # Draw number label
        text(x, origin["y"] + 10, label)

# Draw y-axis
line(origin["x"], 0, origin["x"], HEIGHT)
for y in range(-HEIGHT, 30, 30):
    # Draw vertical tick
    line(origin["x"] - 3, -y, origin["x"] + 3, -y)
    label = y // 30 + 10
    if label != 0:
        # Draw number label
        text(origin["x"] - 10, -y, label)

expr = "x"
color = None

while len(expr) > 0:
    expr = input("Enter an arithmetic expression: ")

    if len(expr) > 0:
        # Set graph color
        color = "red" if not color else "blue" if color == "red" else "green" if color == "blue" else "red"
        setColor(color)

        # Plot points
        x = -13
        while x < 13:
            y = eval(expr)
            rect(origin["x"] + x * 30, origin["y"] - y * 30, 5, 5)
            print("y = {}".format(y))
            x += 0.1
