# Lists []
# list of objects of any type

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
# if we want to print multipay of one itmen without need of writinh it
# repeat an item of list with *
zeros = [0] * 5
# we can combined different type of objects
compined = zeros + letters

# to go over a sequence of numbers we can use list and then range function
numbers = list(range(1, 10))
# to go over a string char to print each of them
chars = list("Hello World")

print(len(chars))  # This one gonna say the string lengh bc of len function
