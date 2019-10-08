##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *
from math import *

# Display size
WIDTH = 800
HEIGHT = 600
# Location of the origin (0, 0) on the screen
ORIGIN = {"x": WIDTH / 2, "y": HEIGHT / 2}
# Num pixels per unit
UNIT = 30
# Num units in the positive/negative x-axis
UNITS_X = 13
UNITS_Y = 10
# How much x increases between each y value
DELTA_X = 0.1

expr = "x"
color = None

# Set background color
background("white")

# Draw x-axis
line(0, ORIGIN["y"], WIDTH, ORIGIN["y"])
for x in range(10, WIDTH, UNIT):
    # Draw horizontal tick
    line(x, ORIGIN["y"] - 3, x, ORIGIN["y"] + 3)

    label = x // UNIT - UNITS_X
    if label != 0:
        # Draw number label
        text(x, ORIGIN["y"] + UNITS_Y, label)

# Draw y-axis
line(ORIGIN["x"], 0, ORIGIN["x"], HEIGHT)
for y in range(-HEIGHT, UNIT, UNIT):
    # Draw vertical tick
    line(ORIGIN["x"] - 3, -y, ORIGIN["x"] + 3, -y)

    label = y // UNIT + UNITS_Y
    if label != 0:
        # Draw number label
        text(ORIGIN["x"] - UNITS_Y, -y, label)


def get_screen_coordinates(px, py):
    return ORIGIN["x"] + px * UNIT, ORIGIN["y"] - py * UNIT


while len(expr) > 0:
    expr = input("Enter an arithmetic expression: ")
    if len(expr) > 0:
        # Set graph color
        color = "red" if not color else "blue" if color == "red" else "green" if color == "blue" else "red"
        setColor(color)

        # Set initial x value at the left side of x-axis
        x = -UNITS_X
        # Set initial y value
        y = eval(expr)
        # Store the x and y values of the previously calculated point
        last = get_screen_coordinates(x, y)
        # Plot points
        while x < UNITS_X:
            y = eval(expr)
            # Draw a line from the last point to the new point
            line(*last, *get_screen_coordinates(x, y))
            last = get_screen_coordinates(x, y)
            x += DELTA_X
