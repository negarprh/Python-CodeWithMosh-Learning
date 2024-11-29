try:
    file = open("app.py")  # Open a File with open function (file object)
    age = int(input("Age? "))
    xfactor = 10 / age
    file.close()  # Close that opend file with close function
except (ValueError, ZeroDivisionError):
    print("You did not enter the valid input")
else:
    print("No exception will thrown")
finally:  # Finally clause will always excecute whatever we have a exception or not, We will use it to release external resourses
    # it is a prefrect place to close files, database connection or network connections
    file.close()
