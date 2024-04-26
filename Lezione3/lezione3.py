#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, 
# you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

pizzas: list = ["Four cheese pizza", "Sausage and fries pizza", "Margherita pizza"]
phrases: list = ["is pretty good.", "is one of my favorites.", "is just okay."]

for i in range(len(pizzas)): print( pizzas[i], phrases[i])

print("I really love pizza!")


#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
# such as Any of these animals would make a great pet!

animals: list = ["Hamsters", "Cats", "Bats"]
phrases: list = ["die easily.", "are worse than dogs.", "are some of the cutest animals that I've ever seen."]

for i in range(len(animals)):
    print( animals[i], phrases[i])

print("All these animals have ears.")


#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1, 21):
    print(i)


#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window).

one_million: list = [i for i in range(1, 100001)]

print(f"First item: {one_million[0]}, and last item: {one_million[-1]}")
'''for i in one_million:
    print(i)'''


#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
#to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

print(f"min: {min(one_million)}. \nmax: {max(one_million)}. \nadd: {sum(one_million)}.")


#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

odd_numbers: list = [i for i in range(1, 21, 2)]

for i in odd_numbers:
    print(i)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_3: list = [i for i in range(3, 31, 3)]

for i in multiples_of_3: print(i)


#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out 
#the value of each cube.

cubes: list = []

for i in range(1, 11):
    cubes.append(i**2)

for i in cubes:
    print(i)
print("\n")

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes_comprehension: list = [i**2 for i in range(1, 11)]

for i in cubes:
    print(i)


#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

x = slice(3)
y = slice(3, 7)
z = slice(7, 10)

print("The list is:", multiples_of_3)
print("The first three items in the list are:", multiples_of_3[x])
print("Three items from the middle of the list are:", multiples_of_3[y])
print("The last three items in the list are:", multiples_of_3[z])


#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
#Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:
#and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are: 
#and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

friend_pizzas: list = ["Four cheese pizza", "Sausage and fries pizza", "Margherita pizza"]

pizzas.append("Neapolitan")
friend_pizzas.append("New York-style")

for i in pizzas:
    print("My favorite pizzas are:", i)
print("\n")
for i in friend_pizzas:
    print("My friend's favorite pizzas are:", i)


#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

#4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
#You won’t use much of it now, but it might be interesting to skim through it.

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

pizzas: list = [
    "Four cheese pizza", "Sausage and fries pizza", "Margherita pizza"
]
phrases: list = [
    "is pretty good.", "is one of my favorites.", "is just okay."
]

for i in range(len(pizzas)):
    print(pizzas[i], phrases[i])

print("I really love pizza!")


multiples_of_3: list = [i for i in range(3, 31, 3)]

for i in multiples_of_3:
    print(i)


one_million: list = [i for i in range(1, 100001)]

print(f"First item: {one_million[0]}, and last item: {one_million[-1]}")

'''for i in one_million:
    print(i)
'''


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.

a_random_list_1: list = [1]
a_random_list_2: list = a_random_list_1

a_random_list_2.append(7)

print("Does lista_1 contains two items? I predict True.")
print(len(a_random_list_1) == 2)
print("Does lista_1 contains one item? I predict False.")
print(len(a_random_list_1) == 1)


a_random_number: int = 3
a_random_number_2: int = a_random_number
a_random_number: int = 9

print("Is a_random_number_2 == 3? I predict True.")
print(a_random_number_2 == 3)
print("Is a_random_number_2 == 9? I predict False.")
print(a_random_number_2 == 9)


v: str = "v"
Scandinavia: str = "Scandinavia"

x = Scandinavia.count(v)

print("Is v in Scandinavia? I predict True.")
print(x == 1)
print("Is there no v in Scandinavia? I predict False.")
print(x == 0)


michael_jackson: dict = {"year" : 1958}

print("Was Michael Jackson born in 1958? I predict True.")
print(michael_jackson["year"] == 1958)
print("Was Michael Jackson born in 1943? I predict False.")
print(michael_jackson["year"] == 1943)


dolly_was_born_in: int = 1946
we_live_in: int = 2024
her_age_is: int = we_live_in - dolly_was_born_in

print("Is Dolly 78 years old? I predict True.")
print(her_age_is == 78)
print("Is Dolly 54 years old? I predict False.")
print(her_age_is == 54)


#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
#If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
#Have at least one True and one False result for each of the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

str_1: str = "We're equal."
str_2: str = "We're equal."

print("Is str_1 == str_2? I predict True.")
print(str_1 == str_2)
print("Is str_1 != str_2? I predict False.")
print(str_1 != str_2)


str_1: str = "UPPER."
str_2: str = "upper."

x = str_1.lower()
y = str_2.count(x)

print("Is str_1 in str_2? I predict True.")
print(y == 1)
print("Is str_1 not in str_2? I predict False.")
print(y == 0)


num_1: int = 78
num_2: int = 56
num_3: int = 83
num_4: int = 64
num_5: int = 28
num_6: int = 28
num_7: int = 53
num_8: int = 90

print("Is num_1 != num_2? I predict True.")
print(num_1 != num_2)
print("Is num_1 == num_2? I predict False.")
print(num_1 == num_2)
print("Is num_3 > num_4? I predict True.")
print(num_3 > num_4)
print("Is num_3 < num_4? I predict False.")
print(num_3 < num_4)
print("Is num_5 == num_6? I predict True.")
print(num_5 == num_6)
print("Is num_5 > num_6? I predict False.")
print(num_5 > num_6)
print("Is num_7 < num_8? I predict True.")
print(num_7 < num_8)
print("Is num_7 == num_8? I predict False.")
print(num_7 == num_8)


str_1: str = "UPPER."
str_2: str = "upper."
a_random_number: int = 3
a_random_number_2: int = a_random_number
a_random_number: int = 9

x = str_1.lower()
y = str_2.count(x)

print("Is str_1 in str_2 and a_random_number_2 == 3? I predict True.")
print(y == 1 and a_random_number_2 == 3)
print("Is str_1 not in str_2 and a_random_number_2 == 9? I predict False.")
print(y == 0 and a_random_number_2 == 9)
print("Is str_1 not in str_2 or a_random_number_2 == 3? I predict True.")
print(y == 0 or a_random_number_2 == 3)


list_1: list = []
list_2: list = list_1

list_2.append(3)

print("Does lista_1 contains an item? I predict True.")
print(len(list_1) == 1)
print("Is lista_1 empty? I predict False.")
print(len(list_1) == 0)


#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 
#'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color: str = "green"

if alien_color == "green":
    print("Congrats! You've just received 5 points.")


alien_color: str = "green"

if alien_color == "green":
    pass


alien_color: str = "red"

if alien_color == "green":
    print("Congrats! You've just received 5 points.")


#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.

alien_color: str = "green"

if alien_color == "green":
    print("Congrats! You've just earned 5 points for shooting the alien.")

else:
     print("Congrats! You've just earned 10 points.")


alien_color: str = "brown"

if alien_color == "green":
    print("Congrats! You've just earned 5 points for shooting the alien.")

else:
     print("Congrats! You've just earned 10 points.")


#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color: str = "green"

if alien_color == "green":
    print("Congrats! You've just earned 5 points.")

elif alien_color == "yellow":
     print("Congrats! You've just earned 10 points.")

elif alien_color == "red":
     print("Congrats! You've just earned 15 points.")


alien_color: str = "yellow"

if alien_color == "green":
    print("Congrats! You've just earned 5 points.")

elif alien_color == "yellow":
     print("Congrats! You've just earned 10 points.")

elif alien_color == "red":
     print("Congrats! You've just earned 15 points.")


alien_color: str = "red"

if alien_color == "green":
    print("Congrats! You've just earned 5 points.")

elif alien_color == "yellow":
     print("Congrats! You've just earned 10 points.")

elif alien_color == "red":
     print("Congrats! You've just earned 15 points.")


#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.
# < 
# >
person_age: int = 58

if person_age < 2:
    print("The person is a baby.")

elif 2 <= person_age < 4:
    print("The person is a toddler.")

elif 4 <= person_age < 13:
    print("The person is a kid.")

elif 13 <= person_age < 20:
    print("The person is a teenager.")

elif 20 <= person_age < 65:
    print("The person is an adult.")

elif person_age > 2:
    print("The person is an elder.")


#5-7. Favorite Fruit: Make a list of your favorite fruits, 
#and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#If the fruit is in your list, the if block should print a statement, such as You really like Apples!

favourite_fruits: list = ["Strawberries", "Cherries", "Bananas", "Yellow kiwis"]
