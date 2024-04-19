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