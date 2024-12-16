class Point:
    # Class Level Attribute
    # We can have Class Attributes too which we define them in class level
    # and they will be same across all instances of the class
    # Not like instance attribute that we can give them different values in the code
    # As methaphor we'll say all human have two eyes
    # And they are shared by all instances
    # We can read this via a class reference or an onject reference
    default_color = "red"

    # Constructor in Point Class
    # We define Two attributes, So Whenever we creaet a new point object, this point object will have these attributes by default
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Here if we change the defualt color, its class refrence. its not point object, its point Class
# Then it says if we change a class level attribute, the change is visible in all objects to that type
Point.default_color = "Yellow"


point = Point(1, 2)

# Object Refrence to get access to Class Level Attribute
print(point.default_color)
# At first output red but after changing the value, yellow

# Also can use point class to get access to class level attribute
print(Point.default_color)

# We also can define an attribute after we create a point object so we can set
# Because Objects in Python are dynamic. We do not have to define all the attributes in the constructor
# We can define them later, whenever we need them
# All of these attributes we define in here, These are all instance attributes
# In Other words, these are attributes that belong to point instances or point objects
# So Every point object can have different values for these attributes

point.z = 10
point.draw()
# Output Point(1,2)

another = Point(3, 4)
another.draw()
# Output: Point(3,4)

print(another.default_color)
# Each Point has its own attributes, Like two people can have different eye color
