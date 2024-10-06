# Logical Operators are: And, Or, Not

high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:  # Not change the value
    print("Eligible for Loan")
else:
    print("Not eligible")

# What is the Short Circuit Evaluation:
# In python Logical Operators are short circuit
# It means when python want to check the value of a statment like and, When the first value is false,
# it does not go and check each of them since in And all of them should be True
# in or operator, when one of them in true it is not gonna go and check all of the value and as soon as it
# sees the True value, it will print the statement
