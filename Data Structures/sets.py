# Sets: is a collection with no duplicate

numbers = [1, 1, 2, 3, 4, 4]
# To remove duplicate element
# conevert list to set
uniques = set(numbers)
print(uniques)
# Output : {1, 2, 3, 4}

# We use {} to define a set
second_set = {1, 4}
# Like lists, we can add new items into a set or remove exisiting one
# To add item
second_set.add(5)
# To remove item
second_set.remove(5)
# To know the length of a set
len(second_set)

# --------------
# Where sets shine are in the powerful mathematical operation supported by them
numbs = [1, 2, 3, 3, 3, 4]
first = set(numbs)
second = {1, 5}

# اجتماع
# Now we can get a union (U) of two sets using vertical bar
# Union will show the items in a new set which include the items that are either in both of thoes two sets
print(first | second)
# OutPut: {1, 2, 3, 4, 5}

# اشتراک
# also we can get the intersction of two different sets
print(first & second)
# Output: {1}

# differenc of two sets
print(first - second)
# Output: {2, 3, 4}

# Semtric Deffirence
# Return the items that are in either first or second but not both
print(first ^ second)
# Output: {2, 3, 4, 5}

# Remember sets unlike lists, they are unorder collection
# Which means items we have in the sets are not sequense so we can not access them using an index
# Means:
# print(first[0]) ---> will be an error
if 1 in first:
    print("Yes")
