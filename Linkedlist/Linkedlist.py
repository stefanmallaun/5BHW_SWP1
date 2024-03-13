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
    - iterator protokoll imlementieren
"""



class Node:
    def __init__(self, data=None):
        # Initialisierung eines neuen Knotens mit Daten und einer Verbindung zum nächsten Knoten (None, wenn es keinen nächsten Knoten gibt)
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialisierung der leeren verketteten Liste mit einem leeren Kopf (head) und der Länge 0
        self.head = None
        self.length = 0

    def append(self, data):
        # Hinzufügen eines Elements am Ende der verketteten Liste
        new_node = Node(data)
        if not self.head:
            # Wenn die Liste leer ist, wird das neue Element der Kopf der Liste
            self.head = new_node
        else:
            # Andernfalls wird das Element an das Ende der Liste angehängt
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def __len__(self):
        # Überschreiben der Länge der verketteten Liste
        return self.length

    def __iter__(self):
        # Iterationsmethode für die verkettete Liste
        self.current = self.head
        return self

    def __next__(self):
        # Methode zum Fortsetzen der Iteration durch die Liste
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def display(self):
        # Methode zum Anzeigen der Elemente der verketteten Liste
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Liste: ", elements)

if __name__ == "__main__":
    # Hauptteil des Codes, der bei Ausführung direkt ausgeführt wird
    linked_list = LinkedList()
    
    # Hinzufügen von 10 zufälligen Elementen zur Liste
    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    # Anzeigen der Länge der Liste und der Elemente
    print("Länge der Liste:", len(linked_list))
    linked_list.display()

    # Iteration durch die Liste und Anzeigen der Elemente
    print("\nDurch die Liste iterieren:")
    for item in linked_list:
        print(item)
