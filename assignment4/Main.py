##
# CPSC 217 Assignment 4
# Name: Anil Mawji
# UCID: 30099809
#
# Program description:

import sys
import math
from SimpleGraphics import *

sys.argv = ['Main.py', 'Baseball.txt']

WIDTH = getWidth()
HEIGHT = getHeight()
PADDING_X = 150
PADDING_Y = 75
SPACING_X = 10
SPACING_Y = 10
BAR_WIDTH = 25
# Colors are taken from https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
COLORS = [
    (230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48), (145, 30, 180), (70, 240, 240),
    (240, 50, 230), (210, 245, 60), (250, 190, 190), (0, 128, 128), (230, 190, 255), (170, 110, 40), (255, 250, 200),
    (128, 0, 0), (170, 255, 195), (128, 128, 0), (255, 215, 180), (0, 0, 128), (128, 128, 128), (255, 255, 255)
]


# Draws a Sankey diagram of a given data set
#
# @param data
# @return
def draw_sankey(data):
    # Calculate bar scale
    total_flow = sum(flow for flow in data.values())
    num_pixels = HEIGHT - PADDING_Y * 2 - (len(data) - 1) * SPACING_Y
    pixels_per_unit = num_pixels / total_flow

    # Draw source bar
    source_x = PADDING_X + SPACING_X
    source_y = (HEIGHT - total_flow * pixels_per_unit) / 2
    setColor(*COLORS[0])
    rect(source_x, source_y, BAR_WIDTH, total_flow * pixels_per_unit)

    destination_x = WIDTH - PADDING_X
    destination_y = PADDING_Y

    for k in data:
        color = COLORS[list(data).index(k) + 1]
        height = data[k] * pixels_per_unit

        # Draw destination text
        setColor("black")
        text(destination_x + BAR_WIDTH + SPACING_X, destination_y + height / 2, k, "w")

        # Draw destination bar
        setColor(*color)
        rect(destination_x, destination_y, BAR_WIDTH, height)

        # Draw body
        offset_y = 0
        increment = (source_y - destination_y) / (destination_x - source_x - BAR_WIDTH)
        range_x = destination_x - source_x - BAR_WIDTH
        for x in range(range_x):
            setColor(x / range_x * color[0],
                     x / range_x * color[1],
                     x / range_x * color[2])
            line(source_x + BAR_WIDTH + x, source_y - offset_y,
                 source_x + BAR_WIDTH + x, source_y + height - offset_y)
            offset_y += increment

        source_y += height
        destination_y += height + SPACING_Y


#
#
# @param file
# @return data
def collect_data(file):
    setColor("black")
    setFont("Calibri", "20")
    text(WIDTH / 2, 50, file.readline())

    setFont("Calibri")
    text(PADDING_X, HEIGHT / 2, file.readline(), "e")

    data = {}
    ln = file.readline()
    while ln:
        line_info = ln.split(",")
        data[line_info[0]] = float(line_info[1])
        ln = file.readline()
    return data


def main():
    setWindowTitle("Assignment 4")
    background("light gray")

    with open(sys.argv[1]) as file:
        draw_sankey(collect_data(file))
        file.close()


if __name__ == '__main__':
    main()
