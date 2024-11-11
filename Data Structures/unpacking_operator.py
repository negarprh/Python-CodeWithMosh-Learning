# with putting * behind numbers, its a unpacking operator
# we unpack a container, pass them as arbitrary arguments to print elements to print function

numbers = [1, 2, 3]
print(*numbers)
# output: instead of [1,2,3] will be 1 2 3

# The thing is that we can unpack any iterable not hust list!

values = [*range(5), *"hello"]
print(values)
# Ouput: [0, 1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']

# Also we can combine multiple lists
first = [1, 2, 3]
second = [3]
print([*second, *first])
# Output: [3, 1, 2, 3]

# Also unpack two dictionary but with **
third = {"x": 1}
forth = {"x": 10, "y": 20}
print({**third, **forth, "z": 30})
# Output: {'x': 10, 'y': 20, 'z': 30}
# remember in unpacking the last value gonna considerd
