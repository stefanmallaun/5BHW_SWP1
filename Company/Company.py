"""
programmiere in Python:

- Bitte UML-Klassendiagramm zeichnen

- eine Firma
- Es gibt Personen, Mitarbeiter, Abteilungsleiter
- Es gibt mehrere Abteilungen, jede(r) Mitarbeiter ist in einer Abteilung
- Es gibt beide Geschlechter
- es gibt nur einen Abteilungsleiter pro Abteilung
- Mitarbeiter gehören immer zu einer Abteilung
- ein Abteilungsleiter ist auch ein Mitarbeiter

- modelliere die Objekte über Vererbung
- erzeuge zum Schluss ein Firmenobjekt

 programmiere folgende Methoden:
 - man muss alle Objekte instanzieren können
 - wieviele Mitarbeiter, Abteilungsleiter gibts in der Firma
 - wieviel Abteilungen gibt es
 - welche Abteilung hat die größte Mitarbeiterstärke
 - wie ist der Prozentanteil Frauen Männer

Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.
Test

"""

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Mitarbeiter(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        self.department = department

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, department, is_Admin):
        super().__init__(name, gender, department)
        self.is_Admin = is_Admin

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.leader = None

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def add_leader(self, leader):
        if self.leader is None:
            self.leader = leader
        else:
            raise ValueError('There can only be one leader in a department')

class Firma:
    def __init__(self):
        self.departments = []
        self.members = []
        self.leaders = []

    def add_department(self, department):
        self.departments.append(department)

    def add_member(self, member):
        self.members.append(member)
        member.department.add_member(member)

    def add_leader(self, leader):
        self.leaders.append(leader)
        self.members.append(leader)
        leader.department.add_leader(leader)

    def count_members(self):
        return len(self.members)

    def count_leaders(self):
        return len(self.leaders)

    def count_departments(self):
        return len(self.departments)

    def department_largest_member_count(self):
        largest_department = max(self.departments, key=lambda x: len(x.members))
        return largest_department.name, len(largest_department.members)

    def percent_distribution_gender(self):
        female_count = len([member for member in self.members if member.gender == 'Female'])
        male_count = len([member for member in self.members if member.gender == 'Male'])
        total_count = len(self.members)

        return {
            'Female': round((female_count / total_count) * 100, 2),
            'Male': round((male_count / total_count) * 100, 2)
        }

    def count_members_company(self):
        return len(self.members)

def main():
    
    firma = Firma()
    
    abteilung1 = Abteilung('Einkauf')
    abteilung2 = Abteilung('Produktion')
    abteilung3 = Abteilung('Verpackung')

    mitarbeiter1 = Mitarbeiter('Hans', 'Male', abteilung1)
    mitarbeiter2 = Mitarbeiter('Anna', 'Female', abteilung2)
    mitarbeiter4 = Mitarbeiter('Anna', 'Female', abteilung2)
    mitarbeiter3 = Mitarbeiter('Peter', 'Male', abteilung3)

    abteilungsleiter1 = Abteilungsleiter('Martha', 'Female', abteilung1, True)
    abteilungsleiter2 = Abteilungsleiter('Michael', 'Male', abteilung2, False)
    abteilungsleiter3 = Abteilungsleiter('Lena', 'Female', abteilung3, True)
    abteilungsleiter3 = Abteilungsleiter('Mario', 'Male', abteilung3, False)

    firma.add_department(abteilung1)
    firma.add_department(abteilung2)
    firma.add_department(abteilung3)

    firma.add_member(mitarbeiter1)
    firma.add_member(mitarbeiter2)
    firma.add_member(mitarbeiter3)
    firma.add_member(mitarbeiter4)

    firma.add_leader(abteilungsleiter1)
    firma.add_leader(abteilungsleiter2)
    firma.add_leader(abteilungsleiter3)

    print('Anzahl Mitarbeiter:', firma.count_members())
    print('Anzahl Abteilungsleiter', firma.count_leaders())
    print('Anzahl Abteilungen:', firma.count_departments())
    print('Größte Abteilung:', firma.department_largest_member_count())
    print('Verteilung der Geschlechter:', firma.percent_distribution_gender())

if __name__ == "__main__":
    main()
