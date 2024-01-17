#map, comprhensive list, lambda


nr = [1,2,3,4,5]

squared_nr = map(lambda x: x*x, nr)
res = list(squared_nr)
print(res)

sqdnr = [i*i for i in nr]

sqdnr1 = list(sqdnr)
print(sqdnr)

class parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class child(parent):
    def __init__(self, name, age, asdf):
        super().__init__(name, age)
        self.asdf = asdf
        
a = child("hey", 12, 12)
print(a)

class abteilungen:
    def __init__ (self):
        elter = []
        kinder = []
    
    
    def addparents(self, elternteil):
        self.elter.append(elternteil)
        
elterteil1 = parent("claudia", 30)
elterteil2 = parent("Josef", 60)

abteilungen.addparents(elterteil1, elterteil1)
addparents(elterteil2)

print(elter)