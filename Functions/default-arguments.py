def increment(number, by=1):  # IMPORTANT : the optional Paramether should be the last one in ( ), i can not put a arequired paramether after it
    return number + by


print(increment(2))  # Output is = 3 since the second argument value is by default 1

print(increment(2, 2))  # output is 4 since we change the default value
