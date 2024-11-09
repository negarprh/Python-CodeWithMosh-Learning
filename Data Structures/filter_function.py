items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 20),
]

# We want to filter out list, like just print the prices in this list greater or equal 10

# filter function is exacly like map function, it gets a (function, iterable)
# it return a iterable again
# we can put it then into a loop to iterate over it or directly put it into list function to put items in a list
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
