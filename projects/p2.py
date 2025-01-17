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
    randHeight = random.uniform(SVG_HEIGHT/1.5, SVG_HEIGHT)
    randWidth = random.uniform(SVG_WIDTH/1.5, SVG_WIDTH)
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

    generateRectangle(800, 800, 2, 2)

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

    # Decides whether or not to randomly split
    splitWidthChance = random.uniform(120, regionWidth * 1.5)
    splitHeightChance = random.uniform(120, regionHeight * 1.5)

    if width < 50 and height < 50:
        return True
    
    else:
        ## IF THE REGION IS REALLY BIG, ALWAYS SPLIT ##
        # Splits into four smaller regions
        if width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2):
            generateRectangle(splitLocationHeight, width, x, y)
            generateRectangle(splitLocationHeight, splitLocationWidth, x, y)
            generateRectangle((height - splitLocationHeight),
                            splitLocationWidth, x, y+splitLocationHeight)
            generateRectangle(height - splitLocationHeight, width -
                            splitLocationWidth, x+splitLocationWidth, y)
        # Two regions split by vertical line
        elif width >= (SVG_WIDTH / 2):
            generateRectangle(height, splitLocationWidth, x, y)
            generateRectangle(height, width-splitLocationWidth,
                          x+splitLocationWidth, y)
        # Two regions split by horizontal line
        elif height >= (SVG_HEIGHT / 2):
            generateRectangle(splitLocationHeight, width, x, y)
            generateRectangle(height-splitLocationHeight,
                          width, x, y+splitLocationHeight)
        ## IF THE REGION IS BIG ENOUGH, MAYBE SPLIT ##
        # Splits into four smaller regions
        elif width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2) and splitWidthChance < regionWidth and splitHeightChance < regionHeight:
            generateRectangle(splitLocationHeight, width, x, y)
            generateRectangle(splitLocationHeight, splitLocationWidth, x, y)
            generateRectangle((height - splitLocationHeight),
                            splitLocationWidth, x, y+splitLocationHeight)
            generateRectangle(height - splitLocationHeight, width -
                            splitLocationWidth, x+splitLocationWidth, y)
        # Two regions split by vertical line
        elif width >= (SVG_WIDTH / 2) and splitWidthChance < regionWidth:
            generateRectangle(height, splitLocationWidth, x, y)
            generateRectangle(height, width-splitLocationWidth,
                          x+splitLocationWidth, y)
        # Two regions split by horizontal line
        elif height >= (SVG_HEIGHT / 2) and splitHeightChance < regionHeight:
            generateRectangle(splitLocationHeight, width, x, y)
            generateRectangle(height-splitLocationHeight,
                          width, x, y+splitLocationHeight)

def main():
    generatePage()


main()