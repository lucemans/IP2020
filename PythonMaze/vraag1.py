##########
## Gebruik volgende functies om te bewegen in de doolhof:
## 
## goForward():
##   Beweeg 1 vakje vooruit
##
## turnRight():
##   Draai een kwartslag naar rechts
##
## turnLeft():
##   Draai een kwartslag naar links
##########

from doolhof import *
import time

# Probleem 1: Manueel uit doolhof gaan
laadDoolhof("doolhof1.txt")
turnRight()
goForward()
turnLeft()
goForward()
goForward()
turnRight()
goForward()
goForward()
turnLeft()
goForward()
goForward()
turnLeft()
goForward()
goForward()
goForward()

time.sleep(5)