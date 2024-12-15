class Point:

    # The constructor is __init__ which is a magic method
    # Is executed when we create a new point object
    # Now we know all the methods we define in class should at least have one parameter which is self by convention
    # Then optionally after we add any additionale parameters for initializing our point object like x and y
    # What is paramether self:
    # Self: is a refrence to the current point object
    # For example in point = Point(1,2), when we call Point Class, Python will internally create the point object in memory
    # And set self to refrence to that point object, now this point object has some bunch of methods that we've been seen before
    # like when we use point. , we'll see all the methods in this point object
    # but an object also can have attributes
    # Attributes: They are basically variables that include data about that object
    # For example we can have x and y attributes that we can easily print on triminal
    # A class or and object bundles data and functions related to that data into one unit
    # As a metaphor, think about a human, Attributes like eye color, height, weight
    # Functions such as walk, talk, eat
    def __init__(self, x, y):
        # Self refrence to current object
        # So use it to set the x and y attributes
        # we can set it to defaut value or this x arguments that recive in this method
        self.x = x
        self.y = y

    def draw(self):
        # Self paramether is refrence to current point object
        # And with this we can read x and y values and print them in terminal
        #
        print(f"Point ({self.x}, {self.y})")


# In here when we create a point object we want to supply initial value for x an y coordinates
# Like point = Point(1,2)
# To achive this we need constructors
# Constructors: a special method that is called when we create a new point object
point = Point(1, 2)


print(point.x)
# Output --> 1

# We dont need to call self like point.draw(point) which is a renfrence to our current point object
# like you dont need to call this paramaehter and python gonna do that for us
point.draw()
# Output --> Point (1, 2)
