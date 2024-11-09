# What is stack
# a linear data structure
# stack is like a books on top of each other, the last one on top is the first one to remove
# We call this behavoir LIFO ---> Last In - First Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# For removing the last item of a list, remeber we used pop function
last = browsing_session.pop()
print(last)
print(browsing_session)  # Print (1,2)
# Remember for calling the last element of a list its [-1] index
print("Redirecting", browsing_session[-1])

# Reminder : 0, "", [] ----> Are faulsy value

if not browsing_session:  # Means if the stack is not empty
    print("disable")
