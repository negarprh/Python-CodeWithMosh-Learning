# It is a try block to handel the exception

try:
    age = int(input("Age? "))
except ValueError as error:  # It is a value error bc the input value is not correct type for example
    print("You did not enter the valid input")
    print(error)  # Output: invalid literal for int() with base 10: 'a'
    print(type(error))  # Output: <class 'ValueError'>
else:
    # Will execute if we dont have any exception, like when the try works
    print("No exception will thrown")
print("Execution Continues")
