list1 = [1, 2, 3]
list2 = [10, 20, 30]

# We wanna combine these two lists in one list where each list is a tuple
# And in the first tuple we will gonna have first element of each list on it
# Zip function gonna do that for us
# Zip gets multiple iterable
print(list(zip(list1, list2)))
# Print [(1, 10), (2, 20), (3, 30)]

# We can add other iterables too
print(list(zip("abc", list1, list2)))
# Print [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
