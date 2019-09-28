##
# CPSC 217 Exercise 2: Home Sweet Home
# Copyright (C) 2019 Anil Mawji

from SimpleGraphics import *

WIDTH = 800
HEIGHT = 600

HOUSE_WIDTH = 400
HOUSE_HEIGHT = 275
HOUSE_X = (WIDTH - 400) / 2
HOUSE_Y = (HEIGHT - 150) / 2

DOOR_WIDTH = 100
DOOR_HEIGHT = HOUSE_HEIGHT - 50
DOOR_X = HOUSE_X + 50
DOOR_Y = HOUSE_Y + HOUSE_HEIGHT - DOOR_HEIGHT

WINDOW_WIDTH = 150
WINDOW_HEIGHT = 100
WINDOW_X = DOOR_X + WINDOW_HEIGHT + 50
WINDOW_Y = (HOUSE_Y + HOUSE_HEIGHT + WINDOW_HEIGHT) / 2

# Draw sky
setColor("turquoise1")
rect(0, 0, WIDTH, 400)

# Draw cloud
setColor("white")
ellipse(25, 50, 75, 75)
ellipse(75, 50, 100, 75)
ellipse(50, 100, 50, 50)
ellipse(75, 100, 100, 75)
ellipse(125, 50, 75, 50)
ellipse(100, 75, 125, 75)

# Draw sun
setColor("yellow")
ellipse(WIDTH - 200, -200, 400, 400)

# Draw grass
setColor("sea green")
rect(0, 400, WIDTH, 200)

setOutline("black")

# Draw the body of the house
setFill("wheat2")
rect(HOUSE_X, HOUSE_Y, HOUSE_WIDTH, HOUSE_HEIGHT)

# Draw roof
setFill("firebrick4")
polygon(
    # Leftmost vertex
    HOUSE_X - 20, HOUSE_Y,
    # Center vertex
    HOUSE_X + HOUSE_WIDTH / 2, HOUSE_Y - 100,
    # Rightmost vertex
    HOUSE_X + HOUSE_WIDTH + 20, HOUSE_Y
)

# Draw door
setFill("navy")
rect(DOOR_X, DOOR_Y, DOOR_WIDTH, DOOR_HEIGHT)

# Draw window
setFill("yellow2")
rect(WINDOW_X, WINDOW_Y, 150, 100)
# Vertical line
line(WINDOW_X + WINDOW_WIDTH / 2, WINDOW_Y, WINDOW_X + WINDOW_WIDTH / 2, WINDOW_Y + WINDOW_HEIGHT)
# Horizontal line
line(WINDOW_X, WINDOW_Y + WINDOW_HEIGHT / 2, WINDOW_X + WINDOW_WIDTH, WINDOW_Y + WINDOW_HEIGHT / 2)

# Sign name
setFont("Times", "14", "bold")
text(WIDTH - 60, HEIGHT - 20, "Anil Mawji")
