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