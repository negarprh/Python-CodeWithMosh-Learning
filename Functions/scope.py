# What is Scope:
# It refers to the region of the code where the variable is defined

message = "b"


def greet(name):
    message = "a"  # the scope of this variable is greet function
    # in simpler words: message varaible just can be called inside of the greet function
    # They are local variables of this function
    # Do not exists anywhere outside of the function


greet("Mosh")
print(message)  # Global Variable have precedence to execute

# Local variables have short life
# means when we for example finish excuting greet function, bc these variable are local and not used anywhere else
# Which means they will garbage collected
# Python intertor will release the memory they allocated for these variables


# Global Variable are accable anywhere in this file
# Store long in memory
