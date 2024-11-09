# Arrays are more effiecent than list if we are dealing with a large sequence of numbers
# And only use them of encounter performance problems

# We need to call it from moudual array, we have a class array there
from array import array

# The first paramether in a arrray is typecode
# Typecode:  is a string of one char that determines the type of objects in your array
# The second parameter of array object is a initializer which in this case is a list of intger
numbers = array('i', [1, 2, 3])
numbers.append(4)
# It has the exact same objects like list, such as append, inser, pop or remove
# also we can access to its different index like:

# But remember, the line down will make a error since every object in this array should be the same type
# numbers[0] = 1.0
