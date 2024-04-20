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


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following,
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

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

print(f"Hi {friends[0]}, how are you?")
print(f"Hi {friends[1]}, how are you?")
print(f"Hi {friends[2]}, how are you?")


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
    print(f"Hi {i}, I'd like to invite you to my house for dinner on Thursday. Kind regards, Nicolò Rufini.")
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
    print(f"Hi {i}, I'd like to invite you to my house for dinner on Thursday. Kind regards, Nicolò Rufini.")
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
    print(f"Hi {i}, I'd like to invite you to my house for dinner on Thursday. Kind regards, Nicolò Rufini.")
print("\n")
