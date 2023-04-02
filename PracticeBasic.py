favorite_language = 'python '
favorite_language1 = favorite_language.strip() #to remove white space from both sides
favorite_language2 = favorite_language.rstrip() #to remove white space from the right side
favorite_language3 = favorite_language.lstrip() #to remove white space from the left side


motorcycles1 = ['honda', 'yamaha', 'suzuki']
#Insert
#this method opens a space at position 0 and stores the value 'ducati' at that location
#this operation shifts every other value in the list one position to the right
motorcycles1.insert(0, 'ducati')
#print(motorcycles1)



#Removing
#If you know the position of the item you want yo remove from a list, you can use the 'del' statement
#when you want to delete an item from a list and not use that item in any way, use the del statement
motorcycles2 = ['honda', 'yamaha', 'suzuki']
del motorcycles2[0]
#print(motorcycles2)



#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
#if you want to use an item as you remove it, use the pop() method.
#you can put index's item inside () at pop to get the item in that position
motorcycles3 = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles3.pop()
popped_motorcycle2 = motorcycles3.pop(1)
#print(motorcycles3)
#print(popped_motorcycle)
#print(popped_motorcycle2)
#print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")



#Sometimes you won’t know the position of the value you want to remove
#from a list. If you only know the value of the item you want to remove, you
#can use the remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
#print(motorcycles)
#print("\nA " + too_expensive.title() + " is too expensive for me.")

#sorting list. sort() sorting a list permanently,  sorted() sorting a list temporarily
#The reverse() method changes the order of a list permanently doesn’t sort backward alphabetically; it simply reverses the order of the list:


squares = []
for value in range(1,11):
    squares.append(value**2)
#print(squares)

#before list but in list comprehensions way
squares1 = [values**2 for values in range(1,11)]
#print(squares1)

#---------------------------------------------------------------------------------------

players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print("Here are the first three players on my team:")
#for player in players[:3]:
#    print(player.title())

#before list but in list comprehensions way
#players1 = [player.title() for player in players[:3]]
#print(players1)

#----------------------------------------------------------------------------------------
#Copying a List
#you can you use list[:] or list.copy(), both work identically
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
#print(my_foods)
#print(friend_foods)

#----------------------------------------------------------------------------------------
#DICTIONARIES
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#when you want to 'for' loop through of a dictionarie, you must be put two variables, in this case (key, value) and use the method 'dictionarie.items()'
#this method return a list of key-value pairs. the for loop then stores each of these pairs in the two variables provided. (key, value)


#Example 1
#for key, value in user_0.items():
    #print("\nKey: " + key)
    #print("Value: " + value)

#Example 2
#for name, language in favorite_languages.items():
    #print(name.title() + "'s favorite language is " + language.title() + ".")


#loop throught all the keys in a dictionary (when you want only the dictionary's keys) you can ommit the method .keys() if you want,
#looping through the keys is actually the default behavior

#Example 1
#for name in favorite_languages.keys():
    #print(name.title())


#Example 2
#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
    #print(name.title())

    #if name in friends:
        #print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

#Example 3
#You can also use the keys() method to find out if a particular person was polled.
#This time, let's find out if Erin took the poll

#if 'erin' not in favorite_languages.keys():
    #print("Erin, please take our poll!")


#Looping through a dictionary's keys in order

#Example1
#for name in sorted(favorite_languages.keys()):
    #print(name.title() + ", thank you for talking the poll.")

#Looping Through All Values in a Dictionary

#Example1
#print("\nThe following languages have been mentioned:")
#for language in favorite_languages.values():
    #print(language.title())


#Example2 (whitout repetition)
#print("\nThe following languages have been mentioned:")
#for language in set(favorite_languages.values()):
    #print(language.title())

#Nesting
# Make an empty list for storing aliens.
#aliens = []

# Make 30 green aliens.
#for alien_number in range(30):
    #new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    #aliens.append(new_alien)

#for alien in aliens[0:3]:
    #if alien['color'] == 'green':
        #alien['color'] = 'yellow'
        #alien['speed'] = 'medium'
        #alien['points'] = 10


#for alien in aliens[0:5]:
    #print(alien)

#print("...")

#A list in a Dictionary
# Store information about a pizza being ordered.
#pizza = {
    #'crust': 'thick',
    #'toppings': ['mushrooms', 'extra cheese'],
#}

#sumarize the order
#print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

#for topping in pizza['toppings']:
    #print("\t" + topping)

#Example2
#favorite_languagesN = {
    #'jen': ['python', 'ruby'],
    #'sarah': ['c'],
    #'edward': ['ruby', 'go'],
    #'phil': ['python', 'haskell'],
#}

#for name, languages in favorite_languagesN.items():
    #print("\n" + name.title() + "'s favorite languages are")
    #for language in languages:
        #print("\t" + language.title())

#A Dictionary in a Dictionary
"""
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
"""

#--------------------------------------------------------------------------
#input
"""
prompt = 'If you tell us who you are, we can personalized the messages you see.'
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
"""

"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
"""

#------------------------------------------------------------------------
#While loops

"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""

"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
"""

#Using a Flag
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
"""
#Using break to Exit a Loop

"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
"""

#Using continue in a Loop

"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #the 'continue' statement tells Python to ignore the rest of the loop and return to the beginning.
    print(current_number)
"""

#Moving items from One list to Another

"""
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    # As the list of unconfirmed users shrinks, the list of confirmed users grows. When the list of
    # unconfirmed users is empty, the loop stops and the list of confirmed users is printed:

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

"""
#Removing all instances of specific Values from a list

"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
"""

#Filling a Dictionary with User Input

"""
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\n What is your name?: ")
    reponse = input("Which mountain would you like to climb someday?: ")

    # Store the response in the dictionary:
    responses[name] = reponse

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
"""


#---------------------------------------------------
#Chapter 8 FUNCTIONS (page 134)
#Defining a Function