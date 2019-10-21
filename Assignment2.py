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
SCALE = 30
# Colors to use when drawing the graph
COLORS = ["red", "blue", "green"]

# Location of the origin (0, 0) on the screen
ORIGIN_X = WIDTH // 2
ORIGIN_Y = HEIGHT // 2
# Num units in the positive/negative x-axis
UNITS_X = WIDTH // SCALE // 2
# Num units in the positive/negative y-axis
UNITS_Y = HEIGHT // SCALE // 2
# How much x increases between each calculation of y
DELTA_X = 0.2

expr = "x"
color_index = 0
# Set background color
background("white")

# Draw x-axis
line(0, ORIGIN_Y, WIDTH, ORIGIN_Y)
for x in range(10, WIDTH, SCALE):
    # Draw horizontal tick 6 pixels tall
    line(x, ORIGIN_Y - TICK_SIZE / 2, x, ORIGIN_Y + TICK_SIZE / 2)

    label = x // SCALE - UNITS_X
    if label != 0:
        # Draw number label
        text(x, ORIGIN_Y + UNITS_Y + TICK_SIZE / 2, label)

# Draw y-axis
line(ORIGIN_X, 0, ORIGIN_X, HEIGHT)
for y in range(-HEIGHT, SCALE, SCALE):
    # Draw vertical tick 6 pixels wide
    line(ORIGIN_X - TICK_SIZE / 2, -y, ORIGIN_X + TICK_SIZE / 2, -y)

    label = y // SCALE + UNITS_Y
    if label != 0:
        # Draw number label
        text(ORIGIN_X - UNITS_Y - TICK_SIZE / 2, -y, label)


# Converts x and y values to their corresponding position on the screen
# @param px     an x value on a graph
# @param py     the y value calculated from the expression
# @param return the position of px and py on the screen
def get_screen_coordinates(px, py):
    return ORIGIN_X + px * SCALE, ORIGIN_Y - py * SCALE


# Draws a curve to the screen
# @param equation of the function to be drawn
def draw_function(expression):
    # Set initial x value at the left side of x-axis
    x = -UNITS_X
    # Stores the x and y values of the previously calculated point
    last_pt = x, eval(expression)
    # Plot points

    while x < UNITS_X:
        current_pt = x, eval(expression)
        # Unpack the coordinates of the last and the new point
        # Draw a line from the last point to the new point
        line(*get_screen_coordinates(*last_pt),
             *get_screen_coordinates(*current_pt))

        x += DELTA_X
        next_pt = x, eval(expression)
        draw_extrema(last_pt, current_pt, next_pt)
        last_pt = current_pt


# Checks if a point is a max or min based on the points before and after it
# @param last_point    the point on the graph that comes prior to current_point
# @param current_point the current point being checked
# @param next_point    the point on the graph that follows current_point
def draw_extrema(last_point, current_point, next_point):
    slope_last = (current_point[1] - last_point[1]) / DELTA_X
    slope_next = (next_point[1] - current_point[1]) / DELTA_X

    # Local minimum
    if slope_last < 0 < slope_next:
        setColor("purple")
        ellipse(*get_screen_coordinates(current_point[0] - DELTA_X / 2, current_point[1]), 5, 5)
    # Local maximum
    elif slope_last > 0 > slope_next:
        setColor("orange")
        ellipse(*get_screen_coordinates(current_point[0] - DELTA_X / 2, current_point[1]), 5, 5)
    # Reset color setting
    setColor(COLORS[color_index])


while expr != "":
    expr = input("Enter the expression (blank line to quit):\ny = ")
    if expr == "":
        close()
        exit(0)

    # Set graph color
    setColor(COLORS[color_index])
    # Sketch curve
    draw_function(expr)
    # Update graph color
    color_index = color_index + 1 if color_index + 1 < len(COLORS) else 0
