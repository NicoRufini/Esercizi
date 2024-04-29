#Nicolò Rufini
#18/4/2024

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, 
#such as, “Hello Eric, would you like to learn some Python today?”

name: str = "Bob"

print(f"Hello {name}, would you like to learn some Python today?")


#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name: str = "Luca"

print(name.lower())
print(name.upper())
print(name)


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: 
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")


#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str= "Albert Einstein"
message: str= "A person who never made a mistake never tried anything new."

print(f"{famous_person} once said: \"{message}\"")


#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, 
#like some file browsers do.

filename: str = "python_notes.txt"

print(filename.removesuffix(".txt"))


#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

friends: list = ["Giampiero", "Giancarlo", "Lucrezio"]

for i in friends:
    print(i)


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.

for i in friends:
    print(f"Hi {i}, how are you?")


#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

Transportations: list = ["Toyota", "Kawasaki", "Wally"]

print(f"{Transportations[0]} seems a preety cool car, I'd like to own one in the future.")
print(f"{Transportations[1]} seems a preety cool motorcycle, I'd like to own one in the future.")
print(f"{Transportations[2]} seems a preety cool boat, I'd like to own one in the future.")
print("\n")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
#Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person,
#inviting them to dinner.

people_I_would_like_to_invite: list = ["Adele", "Albert Einstein", "Alfons Mucha"]

for i in people_I_would_like_to_invite:
    print(f"Hi {i}, I'd like to invite you to a restaurant for dinner on Thursday. Kind regards, Nicolò Rufini.")
print("\n")


#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out 
#a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest 
#  who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

print(f"{people_I_would_like_to_invite[0]} won't be able to go to the dinner.")

people_I_would_like_to_invite[0] = "Amy Winehouse"

for i in people_I_would_like_to_invite:
    print(f"Hi {i}, I'd like to invite you to a restaurant for dinner on Thursday. Kind regards, Nicolò Rufini.")
print("\n")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
#  informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

for i in people_I_would_like_to_invite:
    print(f"Hi {i} I found a bigger dinner table, so I'll invite three more guests.")
print("\n")

people_I_would_like_to_invite.insert(0, "Alicia keys")
people_I_would_like_to_invite.insert(2, "Isaac Newton")
people_I_would_like_to_invite.append("Fred Taylor")

for i in people_I_would_like_to_invite:
    print(f"Hi {i}, I'd like to invite you to a restaurant for dinner on Thursday. Kind regards, Nicolò Rufini.")
print("\n")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
#and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.

print("I can only invite two people for dinner.")

x: str = people_I_would_like_to_invite.pop(5)
print(f"Hi {x}, I'm sorry but you can't go to the dinner.")
x: str = people_I_would_like_to_invite.pop(4)
print(f"Hi {x}, I'm sorry but you can't go to the dinner.")
x: str = people_I_would_like_to_invite.pop(3)
print(f"Hi {x}, I'm sorry but you can't go to the dinner.")
x: str = people_I_would_like_to_invite.pop(2)
print(f"Hi {x}, I'm sorry but you can't go to the dinner.")
print("\n")

for i in people_I_would_like_to_invite:
    print(f"Hi {i}, you're still ivited.")

del people_I_would_like_to_invite[0:]
print(people_I_would_like_to_invite)
print("\n")


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

places_in_the_world: list = ["Kyoto", "Barcelona", "Paris", "Honolu", "Caraibi"]
print(places_in_the_world)

print(sorted(places_in_the_world))
print(places_in_the_world)

print(sorted(places_in_the_world, reverse = True))
print(places_in_the_world)

places_in_the_world.reverse()
print(places_in_the_world)

places_in_the_world.reverse()
print(places_in_the_world)

places_in_the_world.sort()
print(places_in_the_world)

places_in_the_world.sort(reverse = True)
print(places_in_the_world)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message 
#indicating the number of people you’re inviting to dinner.

print(f"The number of people I'm inviting to dinner is {len(people_I_would_like_to_invite)}.")


#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, 
#cities, languages, or anything else you’d like.
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

#Functions introduced: .lower(), .upper(), .removesuffix(), .insert(), .append(), .pop(), del, sorted, .reverse(), 
#.sort(), len()
#Things: google.com, youtube.com, facebook.com

things: list = ["google.com", "youtube.com", "facebook.com"]

for i in things:
    print("Lower case:", i.lower())
    print("Upper case:", i.upper())
    print("Without the suffix:", i.removesuffix(".com"))
    print("\n")

things.insert(0, "instagram.com")
things.append("twitter.com")    
print("New things:", things)


x: str = things.pop(2)
print("Removed item:", x)

del things[2]
print("Things without Facebook:", things)
print("\n")

things.sort()
print("Things in alphabetical order:", things)

things.reverse()
print("Things in reverse-alphabetical order:", things)

print("Things in alphabetical order again:", sorted(things))
print("\n")

print("Numbers of items in things:", len(things))
print("\n")


#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, 
#and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person: dict = {"first_name" : "Giancarlomaria", "last_name" : "Bonadonna", "Age" : 6, "City" : "Bromsgrove"}

print(person)


#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys 
#in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers: dict = {"Gisella" : 46835, "Marinello" : 5135, "Pierfrancesco" : 61194, "Esteban" : 36497, "Vidmer" : 2}

print(favorite_numbers)
print("\n")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, 
#  and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning,
#  or print the word on one line and 
#  then print its meaning indented on a second line. Use the newline character 
# (\n) to insert a blank line between each word-meaning pair in your output.

Glossary: dict = {"Collection" : "A data type that contains multiple items.", "Function" : 
                  "An instruction block that can be called at any point of the program.", "Indentation" : 
                  "The spaces at the beginning of a line that is used to separate informations.", "Loop" : 
                  "A sequence of instructions that repeats itslelf until or as long as a condition is satisfied.", "Algorithm" : 
                  "A sequence of istructions to acomplish a task."}

for i in Glossary:
    print(i + "\n" + Glossary[i] + "\n")


#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, 
#and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, print everything you know about each person.

person_1: dict = {"First name" : "Learco", "Last name" : "Ausserhofer", "Age" : 41, "City" : "Jerash"}
person_2: dict = {"First name" : "Giuliomaria", "Last name" : "Bubbico", "Age" : 76, "City" : "Kigali"}
person_3: dict = {"First name" : "Elio", "Last name" : "Occhipinti", "Age" : 10, "City" : "Jinan"}
people: list = [person_1, person_2, person_3]

for i in people:
    print(i)


#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
#In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
#Next, loop through your list and as you do, print everything you know about each pet. 

pet_1: dict = {"animal" : "dog", "owner_name" : "Manfred"}
pet_2: dict = {"animal" : "hamster", "owner_name" : "Tullio"}
pets: list = [pet_1, pet_2]

for i in pets:
    print(i)


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
#and store one to three favorite places for each person. To make this exercise a bit more interesting, 
#ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places: dict = {"Antonio " : "Luray", "Franca" : "Locarno", "Alberto " : "Cagayan de Oro",}

for i in favorite_places:
    print(i, favorite_places[i], "\n")


#6-10. Favorite Numbers: Modify your program from Exercise 6-2 
#so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers: dict = {"Gisella" : [46835, 6258 ,1480], "Marinello" : [5135, 5405 ,2512], "Pierfrancesco" : [61194, 259 ,60], 
                          "Esteban" : [36497, 23784, 79896], "Vidmer" : [2, 13, 11]}

for i in favorite_numbers:
    print(i, favorite_numbers[i], "\n")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
#and one fact about that city. The keys for each city’s dictionary should be something like country, 
#population, and fact. Print the name of each city and all of the information you have stored about it.

cities: dict = {"New York" : {"Country" : "United States", "Population" : 19571000, 
                             "Fact" : "It's the most linguistically diverse city in the world."}, 
                "Paris" : {"Country" : "France", "Population" : 12272000, 
                           "Fact" : "Paris was originally a Roman City called \"Lutetia\"."}, 
                "Tokyo" : {"Country" : "Japan", "Population" : 37194000, 
                           "Fact" : "There are anti-suicide lights in Tokyo's metro stations."}}

for i in cities:
    print(i, cities[i], "\n")


#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, and extend it by adding new keys and values, 
#changing the context of the program, or improving the formatting of the output.

favorite_places["Jonathan"] = "New York"

print(favorite_places)