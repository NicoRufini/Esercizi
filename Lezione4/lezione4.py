#Let’s try to define a function named subtract ourselves:
#- It should take 2 parameters.
#- Inside the function, it should subtract the two.
#- Then, return the result.
#After you defined it, call the function with some arguments!

def subtract(a: int, b: int) -> int:
    return a - b

print(subtract(5, 2))


#Write a function check_value(), which takes a number as an argument.
#Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.

def check_value(n: int) -> str:
    if n > 5:
        print("The number is bigger than 5")
    elif n < 5:
        print("The number is smaller than 5")
    else:
        print("The number is equal to 5")    

check_value(2)


#Write a function check_length(), which takes a string as an argument.
#Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.

def check_length(s: str) -> str:
    if len(s) > 10:
        print("The string is bigger than 10 characters")
    elif len(s) < 10:
        print("The string is smaller than 10 characters")
    else:
        print("The string is 10 charactes long")    

check_length("1234567890")


#Write a function print_numbers(), which takes a list of numbers as argument. Using a for loop, print each number one by one.

def print_numbers(numbers: list) -> list:
    for i in numbers:
        print(i)

print_numbers([7, 4, 7, 3, 9])


#Write a function check_each(), which takes a list of numbers as argument. Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.

def check_each(numbs: list) -> str:
    for i in range(len(numbs)):
        if numbs[i] > 5:
            print(f"{numbs[i]} is bigger than 5")
        elif numbs[i] == 5:
            print(f"{numbs[i]} is equal to 5")
        else:
            print(f"{numbs[i]} is smaller than 5")

check_each([4, 5, 6])


#Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
#Write another function add_one_to_list(). It takes a list of integers as argument. Define a variable new_list in this function.
#Using a for loop, iterate through the argument list. Using add_one(), fill new_list with integers from the argument list incremented by 1.
#Print new_list.
#Example: add_one_to_list([1, 2, 3]) >>> [2, 3, 4]

def add_one(one: int) -> int:
    one += 1
    return one

print(add_one(3))

def add_one_to_list(list_one: list) -> list:
    new_list = [add_one(list_one[i]) for i in range(len(list_one))]
    return new_list

print(add_one_to_list([7, 8, 12]))


#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about 
#in this chapter. Call the function, and make sure the message displays correctly.

def display_message() -> str:
    print("You're learning about functions.")

display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
#such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title
#as an argument in the function call.

def favorite_book(book_title: str) -> str:
    print(f"One of my favorite books is {book_title}.")

favorite_book("The moving finger")


#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size: str, message: str) -> str:
    print(f"The size of the shirt is a {size}, and the message printed on it is \"{message}\".")

make_shirt("small", "Hi I'm happy:)")
make_shirt(message = "Hi I'm happy:)", size = "small")
print("\n")

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size: str = "large", message: str = "I love Python!") -> str:
    print(f"The size of the shirt is a {size}, and the message printed on it is \"{message}\".")

make_shirt()
make_shirt(size = "medium")
make_shirt(size = "small", message = "This message is on a shirt.")


#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city: str, country: str = "Italy") -> str:
    print(f"{city} is in {country}.")

describe_city("Rome")
describe_city("Milan")
describe_city("Tokyo", "Japan")


#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city: str, country: str) -> str:
    print(f"{city}, {country}.")

city_country("London", "England")
city_country("Beijing", "China")
city_country("Paris", "France")


#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these 
#two pieces of information. Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#Make at least one new function call that includes the number of songs on an album.

def make_album(artist: str, album: str, tracks: list = None) -> dict:
    artist_name: dict = {"Artist" : artist, "Album" : album}

    if tracks:
        artist_name["Tracks"] = tracks

    return artist_name

print(make_album("Adele", "21"))
print(make_album("Silk sonic", "An evening with Silk Sonic"))
print(make_album("Amy Winehouse", "Back to black", ["Tears dry on their own", "Rehab", "He can only hold her"]))


#8-8. User Albums: Start with your program from Exercise 8-7. 
#Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
#Be sure to include a quit value in the while loop.

#It should be "While True:"
while False:
    print(quit)
    print("Enter one of your favorite artist:")
    artist: str = input()
    print("Enter one of their albums:")
    album: str = input()
    print(make_album(artist, album))
    

#8-9. Messages: Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), which prints each text message.

short_messages: list = ["Hi!", "r u ok?", "ah, I'm happy about it"]

def show_messages(messages) -> str:
    for i in messages:
        print(i)

show_messages(short_messages)


#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and moves each message 
#to a new list called sent_messages as it’s printed. After calling the function, 
#print both of your lists to make sure the messages were moved correctly.

sent_messages: list = []

def send_messages(messages: list) -> list:
    for i in short_messages:
        print(i)
        messages.append(i)

send_messages(sent_messages)
print("short_messages:", short_messages)
print("sent_messages:", sent_messages)


#8-11. Archived Messages: Start with your work from Exercise 8-10. 
#Call the function send_messages() with a copy of the list of messages. After calling the function, 
#print both of your lists to show that the original list has retained its messages.

send_messages(sent_messages[:])
print("short_messages:", short_messages)
print("sent_messages:", sent_messages)


#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, 
#and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
#using a different number of arguments each time.

def make_me_a_sandwich(ingredients: list) -> str:
    print("Hi, you ordered a sandwich with:", ingredients)

make_me_a_sandwich(", ".join(["Baked ham", "cheese"]))
make_me_a_sandwich(", ".join(["Hamburger"]))
make_me_a_sandwich(", ".join(["Tomato", "lettuce", "hamburger"]))


#8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
#using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. The function then must return a string 
#such as "Eric Crow, age 45, hair brown, weight 67"

def build_profile(name: str, last_name: str, age: str, hair: str, weight: str) -> dict:
    profile: dict = {"Name" : name, "Last name" : last_name, "Age" : age, "Hair" : hair, "Weight" : weight}
    return f"{profile['Name']} {profile['Last name']}, age {profile['Age']} hair {profile['Hair']} weight {profile['Weight']}"

print(build_profile("Nicolò", "Rufini", "20", "brown", "65"))


#8-14. Cars: Write a function that stores information about a car in a dictionary. 
#The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 

#color: str , "Color" : color.title() , Bluetooth_onnectivity = True,
def make_car(manufacturer: str, model: str, **optional_features) -> dict:
    car: dict = {"Manufacturer" : manufacturer.title(), "Model" : model.title()}

    for option, charcteristic in optional_features.items():
        car[option.title()] = charcteristic

    return car

my_car: dict = make_car("TOYOTA", "AvaLOn", coloR = "red", Bluetooth_connectivity = True)

print(my_car)

''''---------------------------------------------------------------------------------------------------------------------------------'''

#School Grading System:
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, 
#and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.

#Student's name: Bryan, Jennifer, Andrew 
#Subjects: Math, History, Literature

'''Student_1: dict = {}
Student_2: dict = {}
Student_3: dict = {}'''
'''
def School_Grading_System(Student_1: str, Subjects: dict = {"Math" : 56, "History" : 59}) -> str:
    print("name:", Student_1)
    sum = 0
    for i in Subjects:
        print(f"Insert {i} value:", Subjects[i])
        sum += Subjects[i]

    print("Average score:", sum / len(Subjects))
    
    if  sum / len(Subjects) >= 60:
        print("U pass")
    
    else:
        print("U failed")

School_Grading_System("fuys")'''

def School_Grading_System(Stud_1: dict = {"Name" : "Bryan", "Subjects" : {"Math" : 56, "History" : 59}}, 
                          Stud_2: dict = {"Name" : "Jennifer", "Subjects" : {"Math" : 75, "History" : 34}}, 
                          Stud_3: dict = {"Name" : "Andrew", "Subjects" : {"Math" : 67, "History" : 84}}) -> str:
    Students: list = [Stud_1, Stud_2, Stud_3]
    sum = 0
    for i in Students:
        print(i["Name"], "Math:", i["Subjects"]["Math"], "History:", i["Subjects"]["History"])
        sum += i["Subjects"]["Math"] + i["Subjects"]["History"]
        print(sum)
        if  sum / len(Stud_1["Subjects"]) >= 60:
            print(i["Name"], "U pass",  sum / len(Stud_1["Subjects"]))
    
        else:
            print(i["Name"], "U failed",  sum / len(Stud_1["Subjects"]))
        sum = 0

#School_Grading_System()


#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

import random

def Guess_The_Number() -> str:
    the_number: int = random.randrange(1, 50)
    the_guess: int = input("ur guess is: ")
    attempts: int = 0
    maximum_number_attempts: int = 10


    while attempts < maximum_number_attempts:
        if int(the_guess) == the_number:
            print("ur correct")
            break

        elif int(the_guess) > the_number:
            print("too high")
            attempts += 1
            print("attempts", attempts)
            print("repeat")
            if attempts == maximum_number_attempts:
                print("u failed")

            else:
                the_guess: int = input("ur guess is: ")

        elif int(the_guess) < the_number:
            print("too low")
            attempts += 1
            print("attempts", attempts)
            print("repeat")
            if attempts == maximum_number_attempts:
                print("u failed")

            else:
                the_guess: int = input("ur guess is: ")

#Guess_The_Number()


#3. E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

#What do you want to buy?

'''else: 
            print("We're sorry but either we don't have this product or you spelled it wrong, try again")
            x: str = input("What do you want to buy? ")'''

def E_commerce_Shopping_Cart():
    ketchup: dict = {"Name" : "ketchup", "Price" : 4.7}
    Hamburger: dict = {"Name" : "Hamburger", "Price" : 3}
    Potato: dict = {"Name" : "Potato", "Price" : 0.5}
    Products: list = [ketchup, Hamburger, Potato]
    cart: list = []

    print("Here's the products:")

    for i in Products:
        print(i["Name"])

    x: str = input("What do you want to buy? ")

    for i in Products:
        if x.lower() == i["Name"].lower():
            cart.append(i)
            print(cart)

        y: str = input("Do you want to buy soemthing else? ")

        if y.lower() == "yes":
            pass
            

        

#E_commerce_Shopping_Cart()