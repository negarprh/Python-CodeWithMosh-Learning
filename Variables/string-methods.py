course = "  python programming  "

# Functions refers as Methods
# Everything in python is an object
# objects have methods that we can access with .

# Change to upper Case
print(course.upper())
# Just Capitilize the first char of words
print(course.title())
# Remove the extra white space at the words at the begenning and end of the string
print(course.strip())
# remove left white spaces
print(course.lstrip())
# Remove right white spaces
print(course.rstrip())
# Find the index of an specific char, It return the INDEX NUMEBR
print(course.find("mmi"))
# it cannot find it since it return -1 bc Python is case sensetive
print(course.find("Mmi"))
# it replace char m with n
print(course.replace("m", "n"))

# if you wanna chech a char or a sequence of char in your string, it return BOOL Value
print("pro" in course)
print("nro" not in course)
