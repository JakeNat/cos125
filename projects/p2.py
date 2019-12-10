# File: p2.py
# Author: Jake Natalizia
# Date: December 4th, 2019
# Section: B
# Email: jacob.natalizia@maine.edu
# Description: Mondrian Rectangles
# Collaboration: I did not collaborate with anyone.

import random

# CONSTANTS
SVG_WIDTH = 900
SVG_HEIGHT = 900

rect = open('rectangles.html', 'w')


def generatePage():
    randHeight = random.randrange(SVG_HEIGHT/2.5, SVG_HEIGHT)
    randWidth = random.randrange(SVG_WIDTH/2.5, SVG_WIDTH)
    randX = random.randrange(100, SVG_WIDTH/2)
    randY = random.randrange(100, SVG_HEIGHT/2)

    if randX >= randWidth/2:
        randX = random.randrange(100,SVG_WIDTH/3)
    if randY >= randHeight/2:
        randY = random.randrange(100,SVG_HEIGHT/3)

    # Header
    rect.write("""<html>
    <head></head>
    <body>
    """)
    rect.write('<svg width=\"' + str(SVG_WIDTH) +
               '\" height=\"' + str(SVG_HEIGHT) + '\">')

    generateRectangle(randHeight, randWidth, randX, randY)

    # Footer
    rect.write("""

    </svg>
    </body>
</html>""")
    rect.close()

def generateRectangle(height, width, x, y):
    # Color Chooser
    r = random.uniform(0, 0.31)

    if r < 0.0833:
        red = 255
        green = 0
        blue = 0
    elif r < 0.1667 and r > 0.0833:
        red = 51
        green = 255
        blue = 255
    elif r < 0.25 and r > 0.1667:
        red = 255
        green = 255
        blue = 51
    else:
        red = 255
        green = 255
        blue = 255

    rect.write("""
        """)
    rect.write('<rect width=\"' + str(width) + '\" height=\"' +
               str(height) + '\" x=\"' + str(x) + '\" y=\"' + str(y) + '\"')
    rect.write('style="fill:rgb(' + str(red) + ',' + str(green) +
               ',' + str(blue) + ');stroke-width:3;stroke:rgb(0,0,0)"/>\n')

    # Gets region height/width of rectangle
    regionWidth = width - x
    regionHeight = height - y

    # Decides split location
    splitChoice = random.uniform(0.33, 0.67)
    splitLocationWidth = round(splitChoice * regionWidth)
    splitLocationHeight = round(splitChoice * regionHeight)

    # Decides random splits
    randomSplitWidth = random.uniform(120, regionWidth * 1.5)
    randomSplitHeight = random.uniform(120, regionHeight * 1.5)

    
    
    # If the region is really big, ALWAYS split
    if width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2):
        generateRectangle(splitLocationHeight, width, x, y)
        generateRectangle((height - splitLocationHeight),
                          splitLocationWidth, x, y+splitLocationHeight)
        generateRectangle(splitLocationHeight, splitLocationWidth, x, y)
    elif width >= (SVG_WIDTH / 2):
        generateRectangle(height, splitLocationWidth, x, y)
    elif height >= (SVG_HEIGHT / 2):
        generateRectangle(splitLocationHeight, width, x, y)

    # If the region is big enough, maybe split
    elif width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2) and randomSplitWidth < regionWidth and randomSplitHeight < regionHeight:
        generateRectangle(splitLocationHeight, width, x, y)
        generateRectangle((height - splitLocationHeight),
                          splitLocationWidth, x, y+splitLocationHeight)
        generateRectangle(splitLocationHeight, splitLocationWidth, x, y)
    elif width >= (SVG_WIDTH / 2) and randomSplitWidth < regionWidth:
        generateRectangle(height, splitLocationWidth, x, y)
    elif height >= (SVG_HEIGHT / 2) and randomSplitHeight < regionHeight:
        generateRectangle(splitLocationHeight, width, x, y)


def main():
    generatePage()


main()