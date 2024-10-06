# We have For Else when :
# The for loop can not achive sth for example and it breaks out of the loop to achive sth else

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Succesuful")
        break
else:
    print("Attempted Three Times and Failed")
