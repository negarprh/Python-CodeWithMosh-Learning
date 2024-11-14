try:
    age = int(input("Age? "))
    xfactor = 10 / age
# We have another exception handling which is the zero devision error
except (ValueError, ZeroDivisionError):
    print("You did not enter the valid input")
# except ZeroDivisionError: ---> Important point: If there is a error that match the first except, the others will not excecuted
    # print("Age can not be zero")
else:
    print("No exception will thrown")
print("Execution Continues")
