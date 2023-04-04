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
def greet_user(username: str):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

#greet_user('Jessie')

def describe_pet(animal_type: str, pet_name:str):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet(pet_name='harry', animal_type='hamster')

#Default Values
def describe_pet1(pet_name: str, animal_type: str ='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet1(pet_name='willie')

#Return Values
#Making an Argument Optional
def get_formatted_name(first_name: str, middle_name: str, last_name: str):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')

"""To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty
string and move it to the end of the list of parameters: """
def get_formatted_name1(first_name: str, last_name: str, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician1 = get_formatted_name1('jimi', 'hendrix')
musician2 = get_formatted_name1('john', 'hooker', 'lee')

#Returning a Dictionary
def build_person(first_name: str, last_name: str):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician3 = build_person('jimi', 'hendrix')

def buil_person1(first_name: str, last_name: str, age: int =''):
    """Return a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }

    if age:
        person['age'] = age
    return person
musician4 = buil_person1('jimi', 'hendrix', age=27)

#Using a Function with a while Loop
def get_formatted_name2(first_name: str, last_name: str):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#This is an infinite loop!
"""
while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name2(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
"""

#Try It Yourself
"""
# 8.6 City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this
# "Santiago, Chile"
# Call your function with a least three city-country pairs, and print the value that's returned

def city_country(city: str, country: str):
    name_formatted = city + ", " + country
    return name_formatted

#print(city_country(city="Santiago", country="Chile"))

#8.7 Album - 8.8 User Albums
def make_album(artist_name: str, album_title: str, number_tracks = ''):
    music_album = {
        'artist': artist_name,
        'title': album_title,
    }
    if number_tracks:
        music_album['Tracks'] = number_tracks
    return music_album

while True:
    print("\nPlease tell me information about your favourites Albums")
    print("(enter 'q' at any time to quit)")

    ar_name = input("Tell me the artist name: ")
    if ar_name == 'q':
        break

    al_title = input("Tell me the album tittle: ")
    if al_title == 'q':
        break

    nu_track = input("Tell me the Album's track numbers: ")
    if nu_track == 'q':
        break

    making_album = make_album(ar_name, al_title, nu_track)
    print(making_album)
"""

#Passing a list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + str(name).title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']


#Modifying a List in a Function
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, untill none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(complete_models):
    """Show all the models that were printed."""
    print("\nThe Following models have been printed:")
    for complete_model in complete_models:
        print(complete_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


#The slice notation [:] makes a copy of the list to send to the function.
#If we didn’t want to empty the list of unprinted designs.
#we could call print_models() like this:

#print_models(unprinted_designs[:], completed_models)
#show_completed_models(completed_models)

#Passing an Arbitrary Number of Arguments

"""The asterisk in the parameter name '*toppings' tells Python to make an
empty tuple called toppings and pack whatever values it receives into this tuple.
"""
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Mixing positional and Arbitrary Arguments
"""
Python matches positional and keyword arguments first and 
then collects any remaining arguments in the final parameter.
"""
def make_pizza1(size, *toppings):
    """Sumarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with te following toppings:")
    for topping in toppings:
        print("- " + topping)

#make_pizza1(16, 'pepperoni')
#make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments

"""
The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs it
receives into this dictionary.
"""
def buid_profile(first, last, **user_info):
    """Build a dictionary containing everything we knoe about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = buid_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#Storing Your Functions in Modules
