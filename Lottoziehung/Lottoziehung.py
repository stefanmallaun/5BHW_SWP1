import random
import matplotlib.pyplot as plt
import numpy as np

# Funktion, um Lottozahlen zu ziehen
def gamble(n, res):
    if n <= 0:
        print("Die Anzahl der zu ziehenden Zahlen muss positiv sein.")
        return

    max = 45
    num = []

    # Erstellt eine Liste von Zahlen von 0 bis 44
    for i in range(max):
        num.append(i)

    for i in range(n):
        # Zufällige Auswahl einer Indexposition aus der Liste
        index = random.randint(0, max - 1 - i)

        old = num[index]
        new = num[max - 1 - i]

        # Vertauscht die ausgewählte Zahl mit der letzten verbleibenden Zahl in der Liste
        num[index], num[max - 1 - i] = new, old
        res.append(old)

    return res

# Funktion, um die Häufigkeit jeder gezogenen Zahl zu zählen
def statistic(res, dic):
    for i in range(len(res)):
        dic[res[i]] = dic[res[i]] + 1

# Ein leeres Dictionary, um die Häufigkeiten der gezogenen Zahlen zu speichern
dic = {}
for x in range(45):
    dic[x] = 0

tries = 1000

# Führt die Ziehung und die Statistik für eine bestimmte Anzahl von Versuchen (hier 1000) durch
for n in range(tries):
    res = []
    # Zieht 6 Lottozahlen und speichert sie in der 'res'-Liste
    gamble(6, res)
    # Aktualisiert das Dictionary 'dic', um die Häufigkeiten der gezogenen Zahlen zu zählen
    statistic(res, dic)

# Erstellt ein Histogramm der gezogenen Zahlen

print(dic)
plt.bar(dic.keys(), dic.values())
plt.title("Häufigkeit der Lottozahlen, n=" + str(tries))
plt.xlabel("Zahlen")
plt.ylabel("Häufigkeit")
plt.show()
