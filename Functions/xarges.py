# Lists use [] and Tuples use ()
# Both are collection of objects
# Difference: We can not modify tuples, We can not add a new object to tuples
# Both are itreble

def multiply(*numbers):  # with * and then paramether name, we can put multiple items which will be tuples
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
