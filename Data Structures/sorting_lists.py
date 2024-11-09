numbers = [3, 51, 2, 8, 6]

# Sort method gonna sort them in ascending order by default
numbers.sort()
print(numbers)

# Sort then in desending order
# Sort function get two paramether
# sort(key, reverse)
# The reverse paramether can used for reversing the order

numbers.sort(reverse=True)
print(numbers)

# Sort Function, we can pass any iterable and it will sort it for us
# Unlike the sort method, it does not modify th original list
# It will return a new list that is sorted
print(sorted(numbers))

# To change the sort order

print(sorted(numbers, reverse=True))

# A list of Complex Objects
# Every item in this list is a Tuple with two items
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 20),
]

# We Define a Function to sort this list with complex items
# Since each item is a Tuple, We want to sort it based on its price
# Price is the second index = [1]
# All this function does is taking an item, and it returns its price


def sort_item(item):
    return item[1]

# First paramether get from sort function (sort function inside of python) is a key
# we are not calling this function like sort_item(a varible here)
# We are just passing a refrence to this function
# When python attempts to sort this list, it will get each item and it will pass each item into sort_item function
# Which then it return the second index of that list
# Remember write key since we just can pass just keyword arguments, so we need to specifiy our argument that is key, we set it to sort_item


items.sort(key=sort_item)
print(items)
