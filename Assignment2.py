##
# CPSC 217 Assignment 2
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *

WIDTH = 800
HEIGHT = 600

background("white")

# Draw x-axis
line(0, HEIGHT / 2, WIDTH, HEIGHT / 2)
for i in range(-5, WIDTH, 30):
    line(i, HEIGHT / 2 - 3, i, HEIGHT / 2 + 3)

# Draw y-axis
line(WIDTH / 2, 0, WIDTH / 2, HEIGHT)
for i in range(0, HEIGHT, 30):
    line(WIDTH / 2 - 3, i, WIDTH / 2 + 3, i)

expression = input("Enter an arithmetic expression: ")
last = None
x = 0
while x < 26 * 30:
    result = eval("math.cos(%f)" % x) * 30
    print("When x is", x, "the value of the expression is", result)
    line((*last, x, result) if last else (0, 0, x, result))
    last = (x, result)
    x += 30
