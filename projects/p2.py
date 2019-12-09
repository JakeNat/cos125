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
    randHeight  = random.randrange(1,SVG_HEIGHT)
    randWidth = random.randrange(1,SVG_WIDTH)
    randX = random.randrange(1,SVG_WIDTH)
    randY = random.randrange(1,SVG_HEIGHT)

    # Header
    rect.write("""<html>
    <head></head>
    <body>
    """)
    rect.write('<svg width=\"' + str(SVG_WIDTH) + '\" height=\"' + str(SVG_HEIGHT) + '\">')

    generateRectangle(randHeight,randWidth,2,2)

    # Footer
    rect.write("""

    </svg>
    </body>
</html>""")
    rect.close()

def generateRectangle(height,width,x,y):
    rect.write("""
    """)
    rect.write('<rect width=\"' + str(width) + '\" height=\"' + str(height) + '\" x=\"' + str(x) + '\" y=\"' + str(y) + '\"')
    rect.write('style="fill:rgb(255,0,0);stroke-width:3;stroke:rgb(0,0,0)"/>\n')

    # Gets region height/width of rectangle
    regionWidth = width - x
    regionHeight = height - y

    # Decides split location
    splitChoice = random.uniform(0.33,0.67)
    splitLocationWidth = round(splitChoice * regionWidth)
    splitLocationHeight = round(splitChoice * regionHeight)

    # Decides random splits
    randomSplitWidth = random.uniform(120,regionWidth * 1.5)
    randomSplitHeight = random.uniform(120,regionHeight * 1.5)
    # if randomSplitInt < regionWidth: horizontal split
    # if randomSplitInt < regionHeight: vertical split

    # If the region is really big, ALWAYS split
    if width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2):
        generateRectangle(splitLocationHeight,width,x,y)
        generateRectangle((height - splitLocationHeight),splitLocationWidth,x,y+splitLocationHeight)
        generateRectangle(splitLocationHeight,splitLocationWidth,x,y)
    elif width >= (SVG_WIDTH / 2):
        generateRectangle(height,splitLocationWidth,x,y)
    elif height >= (SVG_HEIGHT / 2):
        generateRectangle(splitLocationHeight,width,x,y)    

    # If the region is big enough, maybe split
    elif width >= (SVG_WIDTH / 2) and height >= (SVG_HEIGHT / 2) and randomSplitWidth < regionWidth and randomSplitHeight < regionHeight:
        generateRectangle(splitLocationHeight,width,x,y)
        generateRectangle((height - splitLocationHeight),splitLocationWidth,x,y+splitLocationHeight)
        generateRectangle(splitLocationHeight,splitLocationWidth,x,y)
    elif width >= (SVG_WIDTH / 2) and randomSplitWidth < regionWidth:
        generateRectangle(height,splitLocationWidth,x,y)
    elif height >= (SVG_HEIGHT / 2) and randomSplitHeight < regionHeight:
        generateRectangle(splitLocationHeight,width,x,y)

class Rectangle:
    randWidth = random.randrange(1,SVG_WIDTH)
    randHeight  = random.randrange(1,SVG_HEIGHT)
    randX = random.randrange(1,SVG_WIDTH)
    randY = random.randrange(1,SVG_HEIGHT)

    def __init__(self,h,w,x,y):
        self.height = h
        self.width = w
        self.x = x
        self.y = y

    def generateRectangle(self,h,w,x,y):
        rect.write("""
        """)
        rect.write('<rect width=\"' + str(w) + '\" height=\"' + str(h) + '\" x=\"' + str(x) + '\" y=\"' + str(y) + '\"')
        rect.write('style="fill:rgb(255,0,0);stroke-width:3;stroke:rgb(0,0,0)"/>')

    def getHeight(self):
        return self.height

    def setHeight(self,n):
        if (n>0):
            self.height = n

def main():
    generatePage()
main()