# We have a module name pretty print to make our output pretty, we have control over how we want to print
from pprint import pprint

sentence = "This is a common interview question"

# Dictionary is the best choice because its key value pairs. char is the key  and the repetition is the value
char_frequancy = {}

# Now iterate over each char and update its frequency in this dictinary
for char in sentence:
    if char in char_frequancy:  # If we have the char in the dictionary, inceremenst its frequnecy by 1 update its frequency
        char_frequancy[char] += 1
    # If we dont have it at all, add it for the first time(set it to one)
    else:
        char_frequancy[char] = 1


# pprint(char_frequancy, width=1)
# print(char_frequancy)

# Sort Function gets an iterable
# We pass the dictionary as the iterable
# dictionary.items return key values pairs as a tuples
# By default sort function does not know how to sort dictionary
# Which we have to use the lambda function
# Then key = lambda is an anonmyse function that get the keyValue pair and return the values which we chosen the [1] which is the frequancy of each charachter in the tuple
# Then now sort function know what to sort which is not the [0] and it is the [1]
# Ok now it will sort it from smaller to higher
# We need to reverse it from high to low
# Now when we print it, the first item is the highest on
# DONE
char_frequancy_sorted = (
    sorted(char_frequancy.items(),
           key=lambda kv: kv[1],
           reverse=True))

print(char_frequancy_sorted[0])
