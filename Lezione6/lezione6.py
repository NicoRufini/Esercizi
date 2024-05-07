class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

if alice.age > bob.age:
    print(alice.age)

giampiero = Person("Giampiero G.", 63)
lucrezio = Person("Lucrezio S.", 32)
giovanna = Person("Giovanna H.", 29)
people: list = [alice, bob, giampiero, lucrezio, giovanna]
other_people: list = []

for i in people:
    other_people.append(i.age)
print(min(other_people))


class Student:
    def __init__(self, name: str, studyProgram: str) -> None:
        self.name = name
        self.studyProgram = studyProgram

me = Student("Nicolò", "Fullstack")
on_the_left = Student("Alessandro", "Fullstack") #age 25
on_the_right = Student("Gianmarco", "Fullstack") #age 27