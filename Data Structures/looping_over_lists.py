letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

# If we want to print index of each element, we can call a function enumerate
# This function return the list elemtns with their index as tuples
for letter in enumerate(letters):
    print(letter)

    # output:
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')

# also we can unpack this tuple as :
items = (0, "a")
index, letter = items
# but we can do this unpacking inside the loop as:

for index, letter in enumerate(letters):
    print(index, letter)

    # Output
    # 0 a
    # 1 b
    # 2 c
