#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, 
# you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

pizzas: list = ["Four cheese pizza", "Sausage and fries pizza", "Margherita pizza"]
phrases: list = ["is pretty good.", "is one of my favorites.", "is just okay."]

for i in range(len(pizzas)):
    print( pizzas[i], phrases[i])

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

one_million: list = [i for i in range(1, 1000001)]

print(f"First item: {one_million[0]}, and last item: {one_million[-1]}")
'''for i in one_million:
    print(i)'''