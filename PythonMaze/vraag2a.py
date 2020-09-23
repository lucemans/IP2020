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
##
## freeForward():
##   Kijkt na of er recht voor je een open vakje is (=geen muur)
##
## vooruit/links/rechts wordt altijd vanuit het oogpunt van het pijltje bekeken
##
## while(conditie):
## 	code
##	code
##    Zolang de conditie waar is voer je de lijnen code uit
##########

from doolhof import *
import time

# Vraag 2a: Los doolhof op met while
laadDoolhof("doolhof2a.txt")

while freeForward():
    goForward()
turnRight()
while freeForward():
    goForward()
turnRight()
while freeForward():
    goForward()
turnRight()

time.sleep(5)