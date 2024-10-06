print(type(5))

# This range function returns an object of type range (Return Range Object)
# Range function is iterable, we can iterate over it
print(type(range(5)))
for x in range(5):
    print(x)

# String are iterable too
# In each itration, x holds one character of string Python
for y in "python":
    print(y)

# list are iterable too
# In each itration, z holds one object of list (One item in the list)
for z in [1, 2, 3, 4]:
    print(z)

# Also we can make custum objects that are iterable
# for item in shopping_cart:
#    print(item)

# premetive types are: string, bool, ints
# Complex types: For example range, list --> which use to store a list of objects
