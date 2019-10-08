##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *
from math import *

WIDTH = 800
HEIGHT = 600
ORIGIN = {"x": WIDTH / 2, "y": HEIGHT / 2}

expr = "x"
col = None

background("white")


# Plots a function to the display
# @expression y as a function of x
# @color the color of the graph
def draw_function(expression, color):
    setColor(color)
    # Plot points
    p_x = -13
    while p_x < 13:
        p_y = eval(expression)
        rect(ORIGIN["x"] + p_x * 30, ORIGIN["y"] - p_y * 30, 5, 5)
        print("y = {}".format(p_y))
        p_x += 0.1


# Draw x-axis
line(0, ORIGIN["y"], WIDTH, ORIGIN["y"])
for x in range(10, WIDTH, 30):
    # Draw horizontal tick
    line(x, ORIGIN["y"] - 3, x, ORIGIN["y"] + 3)
    label = x // 30 - 13
    if label != 0:
        # Draw number label
        text(x, ORIGIN["y"] + 10, label)

# Draw y-axis
line(ORIGIN["x"], 0, ORIGIN["x"], HEIGHT)
for y in range(-HEIGHT, 30, 30):
    # Draw vertical tick
    line(ORIGIN["x"] - 3, -y, ORIGIN["x"] + 3, -y)
    label = y // 30 + 10
    if label != 0:
        # Draw number label
        text(ORIGIN["x"] - 10, -y, label)

while len(expr) > 0:
    expr = input("Enter an arithmetic expression: ")
    if len(expr) > 0:
        # Set graph color
        col = "red" if not col else "blue" if col == "red" else "green" if col == "blue" else "red"
        draw_function(expr, col)
