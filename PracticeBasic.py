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
print(squares)

#continue in pague 63 SIMPLE STATISTICS WITH A LIST OF NUMBERS (PYTHON CRASH COURSE)