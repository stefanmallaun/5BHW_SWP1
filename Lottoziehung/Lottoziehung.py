from random import *
from operator import *

def ziehe_lottozahlen():
    gezogene_zahlen = []
    
    while length_hint(gezogene_zahlen) < 6:
        x = randrange(1,45)
        if x not in gezogene_zahlen:
            gezogene_zahlen.append(x)
        
    return gezogene_zahlen

lottozahlen = ziehe_lottozahlen()
print(lottozahlen)
        