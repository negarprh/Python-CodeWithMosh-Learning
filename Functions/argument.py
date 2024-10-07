# What is the difference between the greet and print functions?
# the print function takes input but the greet does not

# now this is a way to pass argument into function
def greet(first_name, last_name):  # the input in the parantesis of a function is parameter
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


# the parameter needs to have value, they are called arguments
greet("Mosh", "Hamedani")
greet("Negar", "Pirasteh")

# Parameter: the input that you define for your function
# Argument: the actual value for the given parameter
