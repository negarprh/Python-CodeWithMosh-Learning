numbers = [1, 2, 3, 4, 5, 6, 7]
# it is the unpacking list
# these two methods of unpacking are the same
# also the left part of the firs method should have the same amount of variables as the list element
# First Way

first, second, third, *other, last = numbers
# other store the rest of list into another list , its packing
print(first, last)
print(other)

# Second way
first = numbers[0]
second = numbers[1]
third = numbers[2]
