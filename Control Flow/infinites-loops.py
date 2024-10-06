# There is two ways to write it

# 1.
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# 2.
# But this one is a infinit loop and infinit loops always have to has a break
# Also they are not efficent for the programs that use a lots of memory since the capetlize memory
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
