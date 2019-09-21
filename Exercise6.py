##
# CPSC 217 Exercise 1: Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji

from SimpleGraphics import *

WIDTH = 800
HEIGHT = 600

# Draw x-axis
line(0, HEIGHT / 2, WIDTH, HEIGHT / 2)
# Draw y-axis
line(WIDTH / 2, 0, WIDTH / 2, HEIGHT)

for i in range(0, 26 * 30, 30):
    # Draw horizontal ticks
    line(i, HEIGHT / 2 - 3, i, HEIGHT / 2 + 3)
    # Draw vertical ticks
    line(WIDTH / 2 - 3, i, WIDTH / 2 + 3, i)
