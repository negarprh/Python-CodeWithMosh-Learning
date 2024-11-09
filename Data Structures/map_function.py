items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 20),
]

# we want to transform this list to another shape
# It is tuple of two items, we want to transform of just its prices

prices = []
for item in items:
    prices.append(item[1])

print(prices)
# with the function we transform or mapped the original list

# With map function
# It takes a (function, iterables), like in out case a lamda and then the list items
# The map function, will apply the lamda fuction on each item in this list
# remeber the map function return a iterable, then before printing we need to put it in the loop to print it
# if we dont make it a list: it print: 10 9 20
# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)
# Beacuse of this we need to pass it also to list function
# Remeber list function can pass any iterable and transform it to a list
prices1 = list(map(lambda item: item[1], items))
print(prices1)
