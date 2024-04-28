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

def describe_city(city: str, country: str = "Italy"):
    print(f"{city} is in {country}.")

describe_city("Rome")
describe_city("Milan")
describe_city("Tokyo", "Japan")

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