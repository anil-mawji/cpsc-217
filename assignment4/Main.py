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
# Colors taken from https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/
COLORS = [
    (230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48), (145, 30, 180), (70, 240, 240),
    (240, 50, 230), (210, 245, 60), (250, 190, 190), (0, 128, 128), (230, 190, 255), (170, 110, 40), (255, 250, 200),
    (128, 0, 0), (170, 255, 195), (128, 128, 0), (255, 215, 180), (0, 0, 128), (128, 128, 128), (255, 255, 255)
]
SOURCE_COLOR = COLORS[1]


# Draws a Sankey diagram of a given data set
#
# @param data
# @return
def draw_sankey(data):
    # Calculate bar scale
    total_flow = sum(flow for flow in data.values())
    num_pixels = HEIGHT - PADDING_Y * 2 - (len(data) - 1) * SPACING_Y
    pixels_per_unit = num_pixels / total_flow

    # Draw the source bar
    source_x = PADDING_X + SPACING_X
    source_y = (HEIGHT - total_flow * pixels_per_unit) / 2
    source_height = total_flow * pixels_per_unit
    setColor(*SOURCE_COLOR)
    rect(source_x, source_y, BAR_WIDTH, source_height)

    # Draw a border around the source bar
    setColor("black")
    line(source_x, source_y, source_x + BAR_WIDTH, source_y)
    line(source_x, source_y, source_x, source_y + source_height)
    line(source_x, source_y + source_height, source_x + BAR_WIDTH, source_y + source_height)

    # Calculate the position of the destination bar
    destination_x = WIDTH - PADDING_X
    destination_y = PADDING_Y

    for k in data:
        # Get the color of the destination bar
        color = COLORS[list(data).index(k) + list(COLORS).index(SOURCE_COLOR) + 1]
        # Calculate the height of the destination bar
        height = data[k] * pixels_per_unit

        # Draw destination bar
        setColor(*color)
        rect(destination_x, destination_y, BAR_WIDTH, height)

        # Draw destination text
        setColor("black")
        text(destination_x + BAR_WIDTH + SPACING_X, destination_y + height / 2, k, "w")

        # Draw body
        range_x = destination_x - source_x - BAR_WIDTH
        for x in range(range_x):
            offset_y = (math.sin(x / range_x * math.pi - math.pi / 2) + 1) / 2 * (source_y - destination_y)
            # Calculate the color of the current line being drawn
            setColor(SOURCE_COLOR[0] + (x / range_x) * (color[0] - SOURCE_COLOR[0]),
                     SOURCE_COLOR[1] + (x / range_x) * (color[1] - SOURCE_COLOR[1]),
                     SOURCE_COLOR[2] + (x / range_x) * (color[2] - SOURCE_COLOR[2]))
            # Draw the current line of the body
            line(source_x + BAR_WIDTH + x, source_y - offset_y,
                 source_x + BAR_WIDTH + x, source_y + height - offset_y)
            # Draw the top border of the body
            setColor("black")
            line(source_x + BAR_WIDTH + x, source_y - offset_y,
                 source_x + BAR_WIDTH + x + 1, source_y - offset_y)
            # Draw the bottom border of the body
            line(source_x + BAR_WIDTH + x, source_y - offset_y + height,
                 source_x + BAR_WIDTH + x + 1, source_y - offset_y + height)

        # Draw border around destination bar
        setColor("black")
        line(destination_x, destination_y, destination_x + BAR_WIDTH, destination_y)
        line(destination_x + BAR_WIDTH, destination_y, destination_x + BAR_WIDTH, destination_y + height)
        line(destination_x, destination_y + height, destination_x + BAR_WIDTH, destination_y + height)

        # Increment the y values to prepare for drawing the next bar
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
