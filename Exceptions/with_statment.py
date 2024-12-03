try:
    # we get acsses to the return to the value of with function with as
    # With statsment python automatically call file.close whether we have finally close or not
    # in other words with statment is used to automatically release external resourses
    with open("app.py") as file, open("another.txt") as target:
        # We can work with the file object in here
        print("File opened.")
        # How it works
        # file object has access to magic methods which start with two __
        # They called magic methods
        # __enter__ and __exit__ magic methods in this section does matter (rest in class section)
        # When an object has these two methods, we say the object support context managment protocol
        # then we can use the object with use with statment
        # Python Will automatically call the exit method and there it will release external resourses
        # That is why we dont need finally clause
        # And then if we wanna do more than one thing like openning a file too, when realising, python will release both these extranal resourses

        file.__
    age = int(input("Age? "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter the valid input")
else:
    print("No exception will thrown")
