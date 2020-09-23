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
## foundExit():
##   Kijkt na of je op de uitgang staat
##
## freeForward():
##   Kijkt na of er recht voor je een open vakje is (=geen muur)
##
## freeRight():
##   Kijkt na of er rechts van je een open vakje is
##
## freeLeft():
##   Kijkt na of er links van je een open vakje is
##
## vooruit/links/rechts wordt altijd vanuit het oogpunt van het pijltje bekeken
##
## while(conditie):
## 	code
##	code
##    Zolang de conditie waar is voer je de lijnen code uit
##########

from doolhof import *

# Vraag 2b: los volgend doolhof op met while
laadDoolhof("doolhof2b.txt")

while(not foundExit()):
    while (freeForward()):
        goForward()  # pas aan!
    turnLeft()
