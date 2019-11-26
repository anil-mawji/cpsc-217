##
# CPSC 217 Assignment 4
# Name: Anil Mawji
# UCID: 30099809
#
# Program description:

from SimpleGraphics import *

WIDTH = getWidth()
HEIGHT = getHeight()


# Draws a sankey diagram given a data set
#
# @param data
# @return
def draw_sankey(data):
    print(data)



def main():
    setWindowTitle("Assignment 4")
    # Set background color of window
    background("light gray")

    data = {}

    with open(input("Enter the name of the file: ") + ".txt") as file:
        for i, line in enumerate(file):
            if i == 0:
                setColor("black")
                setFont("Calibri", "20", "bold")
                text(WIDTH / 2, 40, line)
            elif i == 1:
                setFont("Calibri", "12")
                text(100, HEIGHT / 2, line)
            else:
                line = line.split(", ")
                data[line[0]] = line[1]
        file.close()
    draw_sankey(data)


if __name__ == '__main__':
    main()
