##
# CPSC 217 Assignment 1
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *

WIDTH = 800
HEIGHT = 600
SIZE_X = 500
SIZE_Y = 500

# Position face relative to it's centre
x = int(input("Enter the x position: ")) - SIZE_X / 2
y = int(input("Enter the y position: ")) - SIZE_Y / 2

# Draw background
setColor("deep pink")
rect(0, 0, WIDTH, HEIGHT)

# Draw shadow
setColor("dark magenta")
ellipse(x + 20, y + 20, SIZE_X, SIZE_Y)
# Draw head
setColor("gold")
ellipse(x, y, SIZE_X, SIZE_Y)

# Draw eyes
setColor("yellow4")
pieSlice(x + 75, y + SIZE_Y - 300, 135, 60, 0, 180)
pieSlice(x + SIZE_X - 210, y + SIZE_Y - 300, 135, 60, 0, 180)
# Draw left eyebrow
blob(
    x + 15, y + 240,
    x + 80, y + 160,
    x + 180, y + 125
)
# Draw right eyebrow
blob(
    x + SIZE_X - 15, y + 240,
    x + SIZE_X - 80, y + 160,
    x + SIZE_X - 180, y + 125
)

# Draw mouth
pieSlice(x + 75, y + SIZE_Y - 325, SIZE_X - 150, 250, -180, 180)
# Draw teeth
setColor("white")
pieSlice(x + 75, y + SIZE_Y - 240, SIZE_X - 150, 75, -180, 180)

# Draw left tear
setColor("deep sky blue")
polygon(
    x + 100, y + SIZE_Y - 275,
    x - 8, y + SIZE_Y - 180,
    x + 90, y + SIZE_Y - 150
)
ellipse(x - 20, y + SIZE_Y - 200, 110, 110)
# Draw right tear
polygon(
    x + SIZE_X - 100, y + SIZE_Y - 275,
    x + SIZE_X + 8, y + SIZE_Y - 180,
    x + SIZE_X - 90, y + SIZE_Y - 150
)
ellipse(x + SIZE_X - 90, y + SIZE_Y - 200, 110, 110)
