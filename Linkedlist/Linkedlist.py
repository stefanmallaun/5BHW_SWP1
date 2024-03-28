import random
"""
    Programmiere mit Python, die einfach verkettete Liste als Datenstruktur.

    Folgende Anforderungen sind gegeben:
    - Datenstruktur als Objekt instanzierbar
    - Ganzahl-werte als Werte der Datenstruktur
    - programmiere Methode "am Ende Hinzufügen"
    - programmiere Ausgabe Länge der Datenstruktur
    - Ausgabe aller Elemente
    - main mit exemplarischen (Zufallszahlen) Befüllen
    - iterator protokoll implementieren
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LL:
    
    def __init__(self):
        self.head = None
        self.current = None 
        
    def inserAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.current = new_node
            return
    
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
    
        current_node.next = new_node
    
    
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0
        
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        
def main():
    Linked_list = LL()
    
    for _ in range(10):
        rndm = random.randint(1,100)
        Linked_list.inserAtEnd(rndm)
        
    print("LISTE\n")
    Linked_list.printLL()
    print("\nLänge: ")
    
    length = Linked_list.sizeOfLL()
    print(length)
    
if __name__ == '__main__':
    main()