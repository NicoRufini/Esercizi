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

#da finire


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.legs = None
    
    def set_legs(self, legs: int):
        self.legs = legs

    def get_legs(self):
        return f"there are {self.legs} legs."

horse = Animal("Horse")
horse.set_legs(4)
seahorse = Animal("Seahorse")
seahorse.set_legs(0)

print(horse.name, horse.legs, seahorse.name, seahorse.legs)

horse.legs = 3
seahorse.legs = 2

print(horse.legs, seahorse.legs)
print(horse.get_legs() + "\n" + seahorse.get_legs())


class Food:
    def __init__(self, name: str, price: int, description) -> None:
        self.name = name
        self.price = price
        self.description = description

hampurger = Food("Hambuger", 12, "It has a good taste.")
pasta = Food("Pizza", 2, "")
pizza = Food("Pizza", 20, "")

class Menu:
    def __init__(self, foods: list) -> None:
        self.foods = foods
        foods = []

    def add_food():
        Menu.append()
    
    def remove_food():
        Menu.remove()
    

############33333|356363636