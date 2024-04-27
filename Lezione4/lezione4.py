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


School_Grading_System()


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

Guess_The_Number()
    