# Create a point Class

# Naming of classes: each word is starting with Capital letter and there is no _

class Point:
    # In this block we define all the function that are related to point
    # For example: draw point, move point or get distance between two point

    # Functions in class should at least have a parameter
    # this paramether? self
    def draw(self):
        print("draw")


point = Point()  # This return a point object

print(type(point))
# Output: <class '__main__.Point'> ---> Main is the name of our module

# Is Instance: sometimes we have an object and we want to know
# If this object is an instance of a given class
# For exemaple in here we check if the point object is an instance of the given class
# (Object, Instance of Given Class)
print(isinstance(point, Point))
# Output: True since point object is an instance of the point class
