values = []
for x in range(5):
    values.append(x * 2)

# List comprehension
# [expression (do sth with the item was gotten from the iterate the loop) for item in items]

# Remember this list comperehension is the same as the line above
values_list = [x * 2 for x in range(5)]
# Output: [0, 2, 4, 6, 8]

# Now it has the exact same with set, just insted of [], it should be {}
values_sets = {x * 2 for x in range(5)}
print(values_sets)
# Output: {0, 2, 4, 6, 8}

# Now what is the syntaxical difference between sets and dictionary
# Set: {1,2,3,4} we just have values
# Dictionary: {1: "a", 2: "b"} We have key values that are seprated using a colun

# Now it has the exact same with dictionary, just insted of [], it should be {}
# Here x is the key and x * 2 is the key value
values_dictionary = {x: x * 2 for x in range(5)}
print(values_dictionary)
# Output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# We use line above instead of this:
values_dic = {}
for x in range(5):
    values_dic[x] = x * 2
