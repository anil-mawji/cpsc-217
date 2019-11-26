##
# CPSC 217 Assignment 4
# Name: Anil Mawji
# UCID: 30099809
#
# Program description:

from SimpleGraphics import *

WIDTH = getWidth()
HEIGHT = getHeight()
BAR_WIDTH = 25
PADDING_X = 130
PADDING_Y = 75
SPACING = 10


# Draws a Sankey diagram of a given data set
#
# @param data
# @return
def draw_sankey(data):
    # Calculate bar scale
    total_flow = sum(float(flow) for flow in data.values())
    num_pixels = HEIGHT - PADDING_Y * 2 - (len(data) - 1) * SPACING
    pixels_per_unit = num_pixels / total_flow

    # Draw source bar
    rect(PADDING_X, (HEIGHT - total_flow * pixels_per_unit) / 2, BAR_WIDTH, total_flow * pixels_per_unit)

    # Draw destination rectangles
    offset = 0
    for k in data:
        height = float(data[k]) * pixels_per_unit
        rect(WIDTH - PADDING_X, PADDING_Y + offset, BAR_WIDTH, height)
        text(WIDTH - PADDING_X + BAR_WIDTH * 2, PADDING_Y + offset + height / 2, k)
        offset += height + SPACING


#
#
# @param file
# @return data
def collect_data(file):
    data = {}
    for i, line in enumerate(file):
        if i == 0:
            setColor("black")
            setFont("Calibri", "20")
            text(WIDTH / 2, 50, line)
        elif i == 1:
            setFont("Calibri", "10")
            text(100, HEIGHT / 2, line)
        else:
            line = line.split(", ")
            data[line[0]] = float(line[1])
    return data


def main():
    setWindowTitle("Assignment 4")
    background("light gray")

    with open("Baseball.txt") as file:
    # with open(input("Enter the name of the file: ") + ".txt") as file:
        data = collect_data(file)
        file.close()
    draw_sankey(data)


if __name__ == '__main__':
    main()
