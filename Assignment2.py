##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *
from math import *

# Display size
WIDTH = 800
HEIGHT = 600
# Size of the tick mark on the axes
TICK_SIZE = 6
# Num pixels per unit
UNIT_SIZE = 30
# Colors to use when drawing the graph
COLORS = ["red", "blue", "green"]

# Location of the origin (0, 0) on the screen
ORIGIN = {"x": WIDTH / 2, "y": HEIGHT / 2}
# Num units in the positive/negative x-axis
UNITS_X = WIDTH // UNIT_SIZE // 2
# Num units in the positive/negative y-axis
UNITS_Y = HEIGHT // UNIT_SIZE // 2
# How much x increases between each calculation of y
DELTA_X = 0.2

expr = "x"
color_index = 0
# Set background color
background("white")

# Draw x-axis
line(0, ORIGIN["y"], WIDTH, ORIGIN["y"])
for x in range(10, WIDTH, UNIT_SIZE):
    # Draw horizontal tick 6 pixels tall
    line(x, ORIGIN["y"] - TICK_SIZE / 2, x, ORIGIN["y"] + TICK_SIZE / 2)

    label = x // UNIT_SIZE - UNITS_X
    if label != 0:
        # Draw number label
        text(x, ORIGIN["y"] + UNITS_Y + TICK_SIZE / 2, label)

# Draw y-axis
line(ORIGIN["x"], 0, ORIGIN["x"], HEIGHT)
for y in range(-HEIGHT, UNIT_SIZE, UNIT_SIZE):
    # Draw vertical tick 6 pixels wide
    line(ORIGIN["x"] - TICK_SIZE / 2, -y, ORIGIN["x"] + TICK_SIZE / 2, -y)

    label = y // UNIT_SIZE + UNITS_Y
    if label != 0:
        # Draw number label
        text(ORIGIN["x"] - UNITS_Y - TICK_SIZE / 2, -y, label)


# Converts x and y values to their corresponding position on the screen
# @px an x value on a graph
# @py the y value calculated from the expression
# @return the position of px and py on the screen
def get_screen_coordinates(px, py):
    return ORIGIN["x"] + px * UNIT_SIZE, ORIGIN["y"] - py * UNIT_SIZE


while len(expr) > 0:
    expr = input("Enter the expression (blank line to quit): \ny = ")
    if len(expr) > 0:
        # Set graph color
        setColor(COLORS[color_index])
        print(color_index)
        color_index = color_index + 1 if color_index + 1 < len(COLORS) else 0

        # Set initial x value at the left side of x-axis
        x = -UNITS_X
        # Stores the x and y values of the previously calculated point
        last = get_screen_coordinates(x, eval(expr))
        # Plot points
        while x < UNITS_X:
            y = eval(expr)
            # Unpack the coordinates of the last and the new point
            # Draw a line from the last point to the new point
            line(*last, *get_screen_coordinates(x, y))
            last = get_screen_coordinates(x, y)
            x += DELTA_X
