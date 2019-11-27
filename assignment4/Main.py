##
# CPSC 217 Assignment 4
# Name: Anil Mawji
# UCID: 30099809
#
# Program description:

from SimpleGraphics import *

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
    total_flow = sum(float(flow) for flow in data.values())
    num_pixels = HEIGHT - PADDING_Y * 2 - (len(data) - 1) * SPACING_Y
    pixels_per_unit = num_pixels / total_flow

    # Draw source bar
    source_x = PADDING_X + SPACING_X
    source_y = (HEIGHT - total_flow * pixels_per_unit) / 2
    setColor(*COLORS[0])
    rect(source_x, source_y, BAR_WIDTH, total_flow * pixels_per_unit)

    # Draw destination rectangles
    destination_x = WIDTH - PADDING_X
    destination_y = PADDING_Y
    for k in data:
        height = float(data[k]) * pixels_per_unit

        # Draw destination bar
        setColor(*COLORS[list(data).index(k) + 1])
        rect(destination_x, destination_y, BAR_WIDTH, height)

        # Draw destination text
        setColor("black")
        text(destination_x + BAR_WIDTH + SPACING_X, PADDING_Y + destination_y + height / 2, k, "w")

        # Draw destination body
        polygon(
            source_x + BAR_WIDTH,  # X1
            source_y,  # Y1
            destination_x,  # X2
            destination_y,  # Y2
            destination_x,  # X3
            destination_y + height,  # Y3
            source_x + BAR_WIDTH,  # X4
            source_y + height  # Y4
        )
        source_y += height
        destination_y += height + SPACING_Y


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
            setFont("Calibri")
            text(PADDING_X, HEIGHT / 2, line, "e")
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
