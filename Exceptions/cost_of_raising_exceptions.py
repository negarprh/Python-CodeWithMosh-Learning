# Function timeit imported from moudule time it
# It calculate the execuation time of python code
from timeit import timeit

# Put our code in a multiline string
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age can not be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass

"""
# This function will execute our python code 10,000 times
# Then calculate the execution time and return it
# It reaising the exception, Take more time
print("First Code: ", timeit(code1, number=10000))
# Did not raise exception, faster
print("Second Code: ", timeit(code2, number=10000))

# Then as much as you can, dont use raise exception
