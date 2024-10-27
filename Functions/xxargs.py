# Extended extended Arguments

# So This user objecct in here is a dictionary
def save_user(**user):
    print(user)
    # print(user["id"]) In this case will gonna get the value of the dictionary item like its 1


# Instead of passing arbitrary arguments like (1,2,3,4)
# We can pass keyword arguments
save_user(id=1, name="Titi", age=22)

# Output is = {'id': 1, 'name': 'Titi', 'age': 22}
# It is a Dictionary
# It is a Complex type or a data structure
# With double ** , We can pass multiple key values pairs or keyword arguments
# and Python automatically Package them
