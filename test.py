class Iteratorinho:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            result = self._sequence[self._index]
            self._index += 1
            return result
        
        else:
            raise StopIteration
        
        
def deko(func):
    def wrapper(*a):
        result = func(a)
        return result
    return wrapper
        


class Animal:
    def __init__(self, name):
        self._name = name
        
    def bark():
        pass

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
    
    def bark(self):
        return print("Barks loud")
        
def ColorAlwaysSame(func):
    def wrapper(self, name, color):
        color = "Gelb"
        return func(self, name, color)
    return wrapper
        
class Cat(Animal):
    @ColorAlwaysSame
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
        
    def bark(self):
        return print(f"Doesn't Bark color: {self._color}")

    

dog = Cat("Jack", "red")

print(dog.bark())