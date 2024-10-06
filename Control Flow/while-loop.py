# We use While-loop when we wanna repeat sth as long as the econdition is true

number = 100

while number > 0:
    print(number)
    number //= 2  # Output: 100, 50, 25, 12, 6, 3, 1

# It is like an interactive shell of python who asks you as long as the user wants to quit
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
