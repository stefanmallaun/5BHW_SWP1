#Pokerspielsimulator
#Pokerkarten modellieren
#zufällig fünf Karten ausgeben
#Funktion welche Kombinationen beim Pokerspiel
    #Paar, Drillinge, Poker, Flush, Straße, Royal Flush, ...
#1000 mal spielen und zähle verschiedene Kombinationen
#berechne den prozentuellen Anteil einer Kombination
#richtiger Anteil recherchieren und mit ergebnis vergleichen
import random as r

colors = ['black', 'red']
suits = ['clubs', 'diamonds', 'hearts', 'spades']
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K']

listOfCards = []
card = None

while len(listOfCards) < 5:
    c = r.randint(0, 1)
    s = r.randint(0, 3)
    n = r.randint(0, 12)
    
    # Only clubs and spades can be black
    if (c == 0 and s == 0) or (c == 0 and s == 3) or (c == 1 and s == 2) or (c == 1 and s == 1):
        card = colors[c] + suits[s] + numbers[n]
    
    if card not in listOfCards and card is not None:
        listOfCards.append(card)


print(listOfCards)

