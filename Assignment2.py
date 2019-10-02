##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *

WIDTH = 800
HEIGHT = 600


# Draw x-axis
line(0, HEIGHT / 2, WIDTH, HEIGHT / 2)

for i in range(int(WIDTH / 2), 0, -30):
    line(i, HEIGHT / 2 - 3, i, HEIGHT / 2 + 3)

for i in range(int(WIDTH / 2), WIDTH, 30):
    line(i, HEIGHT / 2 - 3, i, HEIGHT / 2 + 3)

# Draw y-axis
line(WIDTH / 2, 0, WIDTH / 2, HEIGHT)

for i in range(0, HEIGHT, 30):
    line(WIDTH / 2 - 3, i, WIDTH / 2 + 3, i)

equation = input("Enter an equation of x as a function of y: ")
