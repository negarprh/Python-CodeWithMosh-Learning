letters = ["a", "b", "c"]


# Add

# if we want to add an item at the end of a list
# Use APPEND

# remember everything in python is an object, use dot to access functions (methods in that opject)
# When a function is a part of an object, we refer it as an method

letters.append("d")
print(letters)
# Print : ['a', 'b', 'c', 'd']

# if we want to add an element in an specific position
# use INSERT

letters.insert(0, "-a")
print(letters)
# Print : ['-a', 'a', 'b', 'c', 'd']


# Remove

# To remove at the end of a list
# Use POP

letters.pop()
print(letters)
# Print : ['-a', 'a', 'b', 'c']

# Remove base on index number

letters.pop(0)
print(letters)
# Print : ['a', 'b', 'c']

# Remove an element from element value (Remeber it will remove the first occurance of this element, for example first b)
# To remove all b, we have to loop over the list
# Use REMOVE

letters.remove("b")
print(letters)
# Print : ['a', 'c']

# remove a range of items
# Use delet
del letters[0:1]

# To remove all items of a list
# Use Clear
letters.clear()
