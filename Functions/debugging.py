def multiply(*numbers):
    total = 1  # F10 to go over the function
    for number in numbers:
        total *= number
    return total  # if you think it works properly and dont wnat to go over each step, shift+ F11


# Start executing with F5
print("Start")  # Breakpoint F9 then F10
print(multiply(1, 2, 3))  # F11 to see its origin
# finish executing with ctrl + F5
