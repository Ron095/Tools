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

print(pi_string)
print(len(pi_string))

#----------------Continue page 195 Large Files: One Million Digits------------------#










