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

lista_1: list = []
lista_2: list = lista_1

lista_2.append(3)

print("Does lista_1 contains an item? I predict True.")
print(len(lista_1) == 1)
print("Is lista_1 empty? I predict False.")
print(len(lista_1) == 0)


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