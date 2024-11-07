# Tuples: It is a read only list
# () is the sign of the tuple, if we even remove the (), still python see it as a tuple
point1 = (1, 2)
point2 = 1, 2
point3 = 1,  # Tuple with one element
point4 = ()  # Empty tuple
point5 = (1, 2) + (3, 4)  # Concatenate a tuple
point6 = (1, 2) * 3  # To repeat a tuple

# To convert a list to a tuple we'll use a:
# Tuple Function
point7 = tuple([1, 2])
# Since the strings are itreable too will get a tuple with elven char
point8 = tuple("Hello World")
print(point7)  # It will put the list to a tuple and print (1, 2)

# We can access to the item like list
point9 = (1, 2, 3)
print(point9[0])  # Print 1
# To print a range in the tuple with using Slice, print (1,2)
print(point9[0:2])

# We can do unpacking too
x, y, z = point9
if 10 in point9:
    print("Exists")
else:
    print("dont exist")

# In conclusion since we dont have methods to remove or add any object into tuple, then not any of these functions can be used for tuple

# Real world usage:
# If we have a sequence of numebers and we dont want to remove or chenge any item of them accidentily, we will use tuples to avoid any errors
