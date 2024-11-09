x = 10
y = 11
# To swap these variables, we need to store the value of first varibles in the third variable
temp = x
x = y
y = temp
print(f"x is {x} and y is {y}")

# In python, we have one line to do this swaping
# which is tuple unpacking!
a = 1
b = 2
a, b = b, a
print(f"a is {a} and b is {b}")
