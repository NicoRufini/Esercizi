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