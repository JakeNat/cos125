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

def generateHTML():
    # Header

    rect.write("""<html>
    <head></head>
    <body>
    """)
    rect.write('<svg width=\"' + str(SVG_WIDTH) + '\" height=\"' + str(SVG_HEIGHT) + '\">')

    generateRectangle()

    # Footer
    rect.write("""

    </svg>
    </body>
</html>""")
    rect.close()

def generateRectangle():
    randomWidth = random.randrange(1,SVG_WIDTH)
    randomHeight  = random.randrange(1,SVG_HEIGHT)
    randomX = random.randrange(1,SVG_WIDTH)
    randomY = random.randrange(1,SVG_HEIGHT)

    rect.write('<rect width=\"' + str(randomWidth) + '\" height=\"' + str(randomHeight) + '\" x=\"' + str(randomX) + '\" y=\"' + str(randomY) + '\"')
    rect.write('style="fill:rgb(255,0,0);stroke-width:3;stroke:rgb(0,0,0)"/>')

    
def main():
    generateHTML()
main()