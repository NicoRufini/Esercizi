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
    
print("#" * 50)
##################################################

#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

print("(9-1)", "-" * 50)

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self)  -> str:
        print(f"Restaurant = {self.restaurant_name}, Cuisine = {self.cuisine_type}")
    
    def open_restaurant(self) -> str:
        print("The restaurant is open")


restaurant: Restaurant = Restaurant("Moriyama", "Japanese")
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


#9-2. Three Restaurants: Start with your class from Exercise 9-1. 
#Create three different instances from the class, and call describe_restaurant() for each instance.

print("(9-2)", "-" * 50)

restaurant_1: Restaurant = Restaurant("Grotta Azzurra Restaurant", "Italian")
restaurant_2: Restaurant = Restaurant("Uptown Veg", "Vegan")
restaurant_3: Restaurant = Restaurant("Patzeria Perfect Pizza", "Pizzeria")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
#and then create several other attributes that are typically stored in a user profile. 
#Make a method called describe_user() that prints a summary of the user’s information. 
#Make another method called greet_user() that prints a personalized greeting to the user. 
#Create several instances representing different users, and call both methods for each user.

print("(9-3)", "-" * 50)

class User:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def describe_user(self) -> str:
        print(f"name = {self.first_name}, surname = {self.last_name}, email = {self.email}, phone number = {self.phone_number}")
    
    def greet_user(self) -> str:
        print(f"Hi {self.first_name} {self.last_name}!")


user_1: User = User("Giampiero", "Bonadonna", "fakeemail@gmail.com", "555-734 586 92 92")
user_2: User = User("Lucrezia", "Martino", "anotherfakeemail@gmail.com", "555-9834 7215 06")

user_1.describe_user()
user_2.describe_user()
user_1.greet_user()
user_2.greet_user()


#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
#and then change this value and print it again. Add a method called set_number_served() 
#that lets you set the number of customers that have been served. Call this method with a new number and print the value again. 
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

print("(9-4)", "-" * 50)

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self)  -> str:
        print(f"Restaurant = {self.restaurant_name}, Cuisine = {self.cuisine_type}")
    
    def open_restaurant(self) -> str:
        print("The restaurant is open")
    
    def set_number_served(self, number_served: int) -> int:
        self.number_served = number_served

    def increment_number_served(self, add_number_served: int) -> int:
        self.add_number_served = add_number_served
        self.number_served += self.add_number_served


#Instance restaurant from 9-1
restaurant: Restaurant = Restaurant("Moriyama", "Japanese")

restaurant.number_served = 7
print("number_served:", restaurant.number_served)

restaurant.number_served = 12
print("number_served:", restaurant.number_served)

restaurant.set_number_served(15)
print("number_served with set_number_served:", restaurant.number_served)

restaurant.increment_number_served(3)
print("number_served with add_number_served:", restaurant.number_served)


#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
#Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
#Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. 
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

print("(9-5)", "-" * 50)

class User:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts: int = 0

    def describe_user(self) -> str:
        print(f"name = {self.first_name}, surname = {self.last_name}, email = {self.email}, phone number = {self.phone_number}")
    
    def greet_user(self) -> str:
        print(f"Hi {self.first_name} {self.last_name}!")

    def increment_login_attempts(self) -> int:
        self.login_attempts += 1

    def reset_login_attempts(self) -> int:
        self.login_attempts = 0


#User from 9-3
user_1: User = User("Giampiero", "Bonadonna", "fakeemail@gmail.com", "555-734 586 92 92")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("login_attempts with increment_login_attempts:", user_1.login_attempts)

user_1.reset_login_attempts()
print("login_attempts with reset_login_attempts:", user_1.login_attempts)


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
#or Exercise 9-4. Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 

print("(9-6)", "-" * 50)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str]) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self) -> str:
        string_flavors: str = "Flavors: "
        for i in range(len(self.flavors)):
            if self.flavors[i] != self.flavors[-1]:
                string_flavors += f"{self.flavors[i].__str__()}, "

        string_flavors += f"{self.flavors[-1].__str__()}"
        
        print(string_flavors)


ice_cream_stand: IceCreamStand = IceCreamStand("Moriyama", "Japanese", ["Chocolate", "Coffee", "Strawberry"])
ice_cream_stand.display_flavors()


#9-7. Admin: An administrator is a special kind of user. 
#Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", 
#and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. 
#Create an instance of Admin, and call your method.

print("(9-7)", "-" * 50)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str) -> None:
        super().__init__(first_name, last_name, email, phone_number)
        self.privileges: list[str] = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self)  -> str:
        string_privileges: str = "Your privileges: "
        for i in range(len(self.privileges)):
            if self.privileges[i] != self.privileges[-1]:
                string_privileges += f"{self.privileges[i].__str__()}, "

        string_privileges += f"{self.privileges[-1].__str__()}"
        
        print(string_privileges)


admin_1: Admin = Admin("Giampiero", "Bonadonna", "fakeemail@gmail.com", "555-734 586 92 92")
admin_1.show_privileges()


#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, 
#that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. 
#Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.

print("(9-8)", "-" * 50)

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
        #self.privileges: list[str] = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self)  -> str:
        string_privileges: str = "Your privileges: "
        for i in range(len(self.privileges)):
            if self.privileges[i] != self.privileges[-1]:
                string_privileges += f"{self.privileges[i].__str__()}, "

        string_privileges += f"{self.privileges[-1].__str__()}"
        
        print(string_privileges)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, privileges: Privileges) -> None:
        super().__init__(first_name, last_name, email, phone_number)
        self.privileges = privileges
    

privileges_1: Privileges = Privileges(["can add post", "can delete post"])
admin_2: Admin = Admin("Lucrezia", "Martino", "anotherfakeemail@gmail.com", "555-9834 7215 06", privileges_1)

admin_2.privileges.show_privileges()


#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. Make a Restaurant instance, 
#and call one of Restaurant's methods to show that the import statement is working properly.

print("(9-10)", "-" * 50)

from restaurant import restaurant_py

restaurant_py.describe_restaurant()


#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

print("(9-11)", "-" * 50)

from admin import admin_py

admin_py.privileges.show_privileges()


#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

print("(9-12)", "-" * 50)

from admin_2 import admin_2_py

admin_2_py.privileges.show_privileges()


#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
#Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
#Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

print("(9-13)", "-" * 50)

import random

class Die:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll_die(self) -> int:
        #self.random_number: int = random.randrange(1, (self.sides + 1))
        print(random.randrange(1, (self.sides + 1)))


die_1: Die = Die()

print("The die is 6-sided:")
die_1.roll_die() #1°
die_1.roll_die() #2°
die_1.roll_die() #3°
die_1.roll_die() #4°
die_1.roll_die() #5°
die_1.roll_die() #6°
die_1.roll_die() #7°
die_1.roll_die() #8°
die_1.roll_die() #9°
die_1.roll_die() #10°
print("\n")

die_1: Die = Die(10)

print("The die is 10-sided:")
die_1.roll_die() #1°
die_1.roll_die() #2°
die_1.roll_die() #3°
die_1.roll_die() #4°
die_1.roll_die() #5°
die_1.roll_die() #6°
die_1.roll_die() #7°
die_1.roll_die() #8°
die_1.roll_die() #9°
die_1.roll_die() #10°
print("\n")

die_1: Die = Die(20)

print("The die is 20-sided:")
die_1.roll_die() #1°
die_1.roll_die() #2°
die_1.roll_die() #3°
die_1.roll_die() #4°
die_1.roll_die() #5°
die_1.roll_die() #6°
die_1.roll_die() #7°
die_1.roll_die() #8°
die_1.roll_die() #9°
die_1.roll_die() #10°


#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
#Randomly select 4 numbers or letters from the list and print a message saying 
#that any ticket matching these 4 numbers or letters wins a prize.

print("(9-14)", "-" * 50)

num_and_lett: list = [2, 76, 26, 69, 42, 9, 93, 5, 90, 1, "d", "f", "h", "i", "v"]

print("Anyone who has the ticket with the following numbers and letters " \
      f"{num_and_lett[1], num_and_lett[10], num_and_lett[3], num_and_lett[7]}, wins a prize.")


#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
#the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
#Write a loop that keeps pulling numbers until your ticket wins. 
#Print a message reporting how many times the loop had to run to give you a winning ticket.

print("(9-15)", "-" * 50)

import random

my_ticket: list = []
winning_ticket: list = [76, 'd', 69, 5]
attempts: int = 0

while my_ticket != winning_ticket:
    my_ticket.clear()

    i: int = 0
    while i < 4:
        my_ticket.append(random.choice(num_and_lett))
        i += 1

    attempts += 1

print("Congrats, You won!" + f"\nWinning ticket: {winning_ticket}" + f"\nMy ticket: {my_ticket}" + "\nAttempts:", attempts)