##
# CPSC 217 Assignment 1
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

from SimpleGraphics import *

# Declare constants
WIDTH = 800
HEIGHT = 600
SIZE_X = 500
SIZE_Y = 500
EYE_WIDTH = 135
EYE_HEIGHT = 60

# Position head relative to it's centre
x = int(input("Enter the x position: ")) - SIZE_X / 2
y = int(input("Enter the y position: ")) - SIZE_Y / 2

# Draw background
background("deep pink")

# Draw shadow
setColor("dark magenta")
ellipse(x + 20, y + 20, SIZE_X, SIZE_Y)
# Draw head
setColor("gold")
ellipse(x, y, SIZE_X, SIZE_Y)

# Draw left eye
setColor("yellow4")
pieSlice(x + 75, y + SIZE_Y - 300, EYE_WIDTH, EYE_HEIGHT, 0, 180)
# Draw left eye blob of left eye
blob(
    x + 75,  y + SIZE_Y / 2,
    x + 140, y + SIZE_Y / 2 - 35,
    x + 75,  y + SIZE_Y / 2 - 35
)
# Draw right eye blob of left eye
blob(
    x + SIZE_X - 215 - 75,  y + SIZE_Y / 2,
    x + SIZE_X - 215 - 140, y + SIZE_Y / 2 - 35,
    x + SIZE_X - 215 - 75,  y + SIZE_Y / 2 - 35
)

# Draw right eye
pieSlice(x + SIZE_X - 210, y + SIZE_Y - 300, EYE_WIDTH, EYE_HEIGHT, 0, 180)
# Draw left eye blob of right eye
blob(
    x + 215 + 75,  y + SIZE_Y / 2,
    x + 215 + 140, y + SIZE_Y / 2 - 35,
    x + 215 + 75,  y + SIZE_Y / 2 - 35
)
# Draw right eye blob of right eye
blob(
    x + SIZE_X - 75,  y + SIZE_Y / 2,
    x + SIZE_X - 140, y + SIZE_Y / 2 - 35,
    x + SIZE_X - 75,  y + SIZE_Y / 2 - 35
)

# Draw left eyebrow
blob(
    x + 15,  y + 240,
    x + 80,  y + 160,
    x + 180, y + 125
)
# Draw right eyebrow
blob(
    x + SIZE_X - 15,  y + 240,
    x + SIZE_X - 80,  y + 160,
    x + SIZE_X - 180, y + 125
)

# Draw mouth
pieSlice(x + 75, y + SIZE_Y - 325, SIZE_X - 150, 250, 0, -180)
# Draw teeth
setColor("white")
pieSlice(x + 75, y + SIZE_Y - 240, SIZE_X - 150, 75, 0, -180)

# Draw left tear
setColor("deep sky blue")
polygon(
    x + 100, y + SIZE_Y - 275,
    x - 8,   y + SIZE_Y - 180,
    x + 90,  y + SIZE_Y - 150
)
ellipse(x - 20, y + SIZE_Y - 200, 110, 110)
# Draw right tear
polygon(
    x + SIZE_X - 100, y + SIZE_Y - 275,
    x + SIZE_X + 8,   y + SIZE_Y - 180,
    x + SIZE_X - 90,  y + SIZE_Y - 150
)
ellipse(x + SIZE_X - 90, y + SIZE_Y - 200, 110, 110)

# Sign name
setColor("black")
setFont("Times", "14", "bold")
text(WIDTH - 60, HEIGHT - 20, "Anil Mawji")
