items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 20),
]

prices = list(map(lambda item: item[1], items))

filtered = list(filter(lambda item: item[1] >= 10, items))

# List comprehesion is just for python to do the job of function map or filterd
# it is [expression and then for loop]

# list comprehension of map functions:
prices_comprehension = [item[1] for item in items]
# Exectly print the same line as above for map function  [10, 9, 20]
print(prices_comprehension)

# list comprehension of filter functions:
filtered_comprehension = [item for item in items if item[1] >= 10]
# Exectly print the same line as above for filter function  [('Product1', 10), ('Product3', 20)]
print(filtered_comprehension)
