# To get the size of an object
from sys import getsizeof

values = [x * 2 for x in range(10)]
for x in values:
    print(x)

# Output: even numbers from 0 to 18

# But what if the range was a milion
# it was not efficent to store all of the objects in the memory as a list
# Better and more effiecent way? store them as a generator object
# Generator object: Iterable like list and in each generation, we generate or spit out a new value
# Unlike list they dont store values in iterations, they generate a new value in each iteration

values_generator = (x * 2 for x in range(10))  # just have ()
for x in values_generator:
    print(x)


values_generator_size = (x * 2 for x in range(1000))
print("generator size", getsizeof(values_generator_size))
# output is 120 , which is the byte in memory
# it does not matter how much is the range, it will always be the 120 byte since with each iteration it store the value


values_list_size = [x * 2 for x in range(1000)]
print("list size", getsizeof(values_list_size))
# Output: list size 8856
# which means how much is a lot in comparison with generator

# BE CUATION
# it does not store the size of the values in generator
# Then when we call len, it does not show the length of it and its error
