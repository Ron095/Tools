#-----------------------Chapter 10---------------------#
#--------------FILES AND EXCEPTIONS-------------*
#The only difference between this output and the original file is the
#extra blank line at the end of the output. The blank line appears because
#read() returns an empty string when it reaches the end of the file; this empty
#string shows up as a blank line. If you want to remove the extra blank line,
#you can use rstrip() in the print statement:

file_path = 'C:/Users/RONALD/Documents/Python Projects/ToolsProjects/text_files/pi_digits.txt'
#with open(file_path) as file_object:
    #contents = file_object.read().rstrip()

#Reading Line by line
"""
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
"""

#Making a List of Lines from a file
"""
When you use with, the file object returned by open() is only available inside
the with block that contains it. If you want to retain access to a file’s contents
outside the with block, you can store the file’s lines in a list inside the block
and then work with that list. You can process parts of the file immediately
and postpone some processing for later in the program.
"""
#the readlines() method takes each line from the file and stores it
#in a list. This list is then stored in lines, which we can continue to work with
#after the with block ends.

with open(file_path) as file_object:
    lines = file_object.readlines()

#Working with a File's Contents
"""
When Python reads from a text file, it interprets all text in the file as a string. If you
read in a number and want to work with that value in a numerical context, you’ll
have to convert it to an integer using the int() function or convert it to a float using
the float() function.
"""

pi_string = ''
for line in lines:
    pi_string += line.strip()

#print(pi_string)
#print(len(pi_string))

#----------------Continue page 195 Large Files: One Million Digits------------------#
#print(pi_string[:52] + "...")

#Is your Birthday Contained in Pi?
"""
birthday = input('Enter your birthday, in the from mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
"""

#Writing to a File
#Writing to an Empty File

"""
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
"""

#Writing Multiple Lines
"""
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
"""
#Appending to a File
"""
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
"""
#Exceptions
#Handing the ZeroDivisionError Exception
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
"""
#Using Exceptions to Prevent Crashes
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
"""

#Handing the FileNotFoundError Exception

"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
"""

#Analyzing Text

"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
"""

#Working with Multiple Files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


#filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt']
#for filename in filenames:
    #count_words(filename)

#Failing Silently
def count_words1(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

#filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt']
#for filename in filenames:
    #count_words1(filename)

#Using json.dump() and json.load() ( This is a simple way to share data between two programs.
import json

#json.dump()
#numbers = [2, 3, 5, 7, 11, 13]
#filename = 'numbers.json'
#with open(filename, 'w') as f_obj:
    #json.dump(numbers, f_obj)

#json.load()
#filename = 'numbers.json'
#with open(filename) as f_obj:
    #numbers = json.load(f_obj)
#print(numbers)

#Saving and Reading User-Generated Data
"""
username = input("What is your name? ")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
"""

#Now let's write a new program that greets a user whose name has already been stored:
"""
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
"""