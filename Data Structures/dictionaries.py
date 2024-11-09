# Dictionary : is a data structure in python which is basically is a collection of key value pairs
# There is no type limitation
point = {"x": 1, "y": 2}
list()
tuple()
set()
# another way is use dict function like other functions for other data structures
point = dict(x=1, y=2)
print(point)
# Output: {'x': 1, 'y': 2}

# Note: the index in a dictionary is the name of a key
print(point["x"])
# Output: 1

# We can change the value of a x
point["x"] = 10
print(point)
# Output: {'x': 10, 'y': 2}

# Add a new key
point["z"] = 20
print(point)
# Output: {'x': 10, 'y': 2, 'z': 20}

# Check the existance of a key
if "a" in point:
    print(point["a"])
    # No output since it does not exist GIRL

# OR using get function
print(point.get("a"))  # return None
print(point.get("a", 0))  # pass a default value as second argument, return 0

# Delete an item in dictionary
# Use del operation
del point["x"]
print(point)
# Output: {'y': 2, 'z': 20}

# To loop over a dictionary, iterate over a dictionary
for key in point:
    print(key, point[key])
# Output:
# y 2
# z 20

for x in point.items():
    print(x)
# Output:
# ('y', 2)
# ('z', 20)

# then we can unpack it like
for key, value in point.items():
    print(key, value)
# Which we will gonna get the same resule like:
# y 2
# z 20
