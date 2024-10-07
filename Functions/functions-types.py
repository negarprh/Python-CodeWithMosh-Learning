# Types of Functions
# 1. Perform and Carry out a Task
# 2. Calculate and Return a Value


round(1.9)  # Type 2 function


def greet(name):
    # print(f"Hi {name}")  # type 1 function
    return "..."  # it has preseduce of printing rather that the print call we are calling outside of the functions


print(greet("Negar"))  # It retune Hi Negar and None
# None is the return value of greet function
# in python all functions return None value by default
# None is an Object that represents the absence of a value
# If greet had a return even a return "...", it did not retrun None


def get_greeting(name):
    return f"Hi {name}"  # type 2 function, This one is a more felixable version of greet function becuase we did not tie the function just to print sth, it return the value which helps to use this function in other senarias


message = get_greeting("Negar")
print(message)
file = open("content.txt", "w")
file.write(message)
