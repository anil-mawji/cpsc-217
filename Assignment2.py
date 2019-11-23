##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809
#
# Program Description: Graphs mathematical functions given by the user and plots their maximum and minimum points

from SimpleGraphics import *
from math import *

# Display size
WIDTH = getWidth()
HEIGHT = getHeight()
# Size of the tick mark on the axes
TICK_SIZE = 6
# Num pixels per unit
SCALE = 30
# Colors to use when drawing the graph
COLORS = ["red", "blue", "green"]
# Size in pixels to use when drawing points of extrema
EXTREMA_SIZE = 6

# Location of the origin (0, 0) on the screen
ORIGIN_X = WIDTH // 2
ORIGIN_Y = HEIGHT // 2
# Num units in one quadrant of the x-axis
UNITS_X = WIDTH // SCALE // 2
# Num units in one quadrant of the y-axis
UNITS_Y = HEIGHT // SCALE // 2
# How much x increases between each calculation of y
DELTA_X = 0.2


def draw_axes():
    # Set background color
    background("white")
    # Draw x-axis
    line(0, ORIGIN_Y, WIDTH, ORIGIN_Y)
    for x in range(10, WIDTH, SCALE):
        # Draw horizontal tick TICK_SIZE pixels tall
        line(x, ORIGIN_Y - TICK_SIZE / 2, x, ORIGIN_Y + TICK_SIZE / 2)

        label = x // SCALE - UNITS_X
        if label != 0:
            # Draw number label
            text(x, ORIGIN_Y + UNITS_Y + TICK_SIZE / 2, label)

    # Draw y-axis
    line(ORIGIN_X, 0, ORIGIN_X, HEIGHT)
    for y in range(-HEIGHT, SCALE, SCALE):
        # Draw vertical tick TICK_SIZE pixels wide
        line(ORIGIN_X - TICK_SIZE / 2, -y, ORIGIN_X + TICK_SIZE / 2, -y)

        label = y // SCALE + UNITS_Y
        if label != 0:
            # Draw number label
            text(ORIGIN_X - UNITS_Y - TICK_SIZE / 2, -y, label)


# Draws a curve to the screen
#
# @param expression equation of the function to be drawn
# @param color      the color of the function being drawn
def draw_function(expression, color):
    # Set initial x value at the left side of x-axis
    x = -UNITS_X
    # Stores the x and y values of the previously calculated point
    last_pt = x, eval(expression)
    # Plot points

    while x < UNITS_X:
        current_pt = x, eval(expression)
        # Unpack the coordinates of the last and the new points
        # Draw a line from the last point to the new point
        line(*get_screen_coordinates(*last_pt),
             *get_screen_coordinates(*current_pt))
        # Increment x to prepare for drawing the next point
        x += DELTA_X
        next_pt = x, eval(expression)
        draw_extrema(last_pt, current_pt, next_pt, color)
        # Update previous point to prepare for drawing the next point
        last_pt = current_pt


# Converts x and y values to their corresponding position on the screen
#
# @param px     an x value on a graph
# @param py     the y value calculated from the expression
# @return the position of px and py on the screen
def get_screen_coordinates(px, py):
    return ORIGIN_X + px * SCALE, ORIGIN_Y - py * SCALE


# Checks if a point is a max or min based on the points before and after it
#
# @param last_point    the point on the graph that comes prior to current_point
# @param current_point the current point being checked
# @param next_point    the point on the graph that follows current_point
# @param color         the color of the function being drawn
def draw_extrema(last_point, current_point, next_point, color):
    slope_last = (current_point[1] - last_point[1]) / DELTA_X
    slope_next = (next_point[1] - current_point[1]) / DELTA_X

    # Local minimum
    if slope_last < 0 < slope_next:
        setColor("orange")
        position = get_screen_coordinates(*current_point)
        ellipse(position[0] - EXTREMA_SIZE / 2, position[1] - EXTREMA_SIZE / 2,
                EXTREMA_SIZE, EXTREMA_SIZE)
    # Local maximum
    elif slope_last > 0 > slope_next:
        setColor("purple")
        position = get_screen_coordinates(*current_point)
        ellipse(position[0] - EXTREMA_SIZE / 2, position[1] - EXTREMA_SIZE / 2,
                EXTREMA_SIZE, EXTREMA_SIZE)
    # Reset color setting
    setColor(color)


def main():
    # Draw x and y axis
    draw_axes()
    # Get input from user
    expr = input("Enter the expression (blank line to quit):\ny = ")
    color_index = 0
    while expr != "":
        # Close program if input was blank
        if expr == "":
            close()
            exit(0)
        # Set graph color
        setColor(COLORS[color_index])
        draw_function(expr, COLORS[color_index])
        # Prepare new color for drawing the next expression
        color_index = color_index + 1 if color_index + 1 < len(COLORS) else 0
        expr = input("Enter the expression (blank line to quit):\ny = ")


if __name__ == '__main__':
    main()
