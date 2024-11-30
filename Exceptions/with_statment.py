try:
    # we get acsses to the return to the value of with function with as
    # With statsment python automatically call file.close whether we have finally close or not
    # in other words with statment is used to automatically release external resourses
    with open("app.py") as file:
        # We can work with the file object in here
        print("File opened.")
        # How it works
        # file object has access to magic methods which start with two __
        # They called magic methods
        file.__
    age = int(input("Age? "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter the valid input")
else:
    print("No exception will thrown")
