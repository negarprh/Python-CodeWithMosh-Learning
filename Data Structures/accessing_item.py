letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[-1])  # Print d
print(letters[0])  # print the modified version which is A

# Slicing function which we used for the string also can be used for the lists
print(letters[0:3])  # Print ['A','b','c']
print(letters[::2])  # Print every 2 elements like 0, 2 Print --> ['A','c']


numbers = list(range(20))  # print 0 to 20m 20 not included
print(numbers[::2])  # Print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Print elemnts in reverse [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1])
