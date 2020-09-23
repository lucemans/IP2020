from PIL import Image

im = Image.open('image2.png')
pix = im.load()
width, height = im.size

threshhold = 10

finalText = ''
hasStarted = False
hasEnded = False

for y in range(height):
    row = ''
    for x in range(width):
        red, blue, green, alpha = pix[x, y]
        if ((red+blue+green)/3 > threshhold):
            if (not hasStarted):
                row += 'S'
                hasStarted = True
            elif (not hasEnded):
                row += 'E'
                hasEnded = True
            else:
                row += ' '
        else:
            row += '#'
        # row += ' ' if (red+blue+green)/3 > (threshhold) else '#'
    print(row)
    finalText += row + '\n'

text_file = open("doolhof_custom.txt", "w")
n = text_file.write(finalText)
text_file.close()

from doolhof import *
laadDoolhof("doolhof_custom.txt")

input()
