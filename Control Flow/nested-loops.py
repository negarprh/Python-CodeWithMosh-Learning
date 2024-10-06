# How this Loop works
# There are two loops, Outer and the inner Loop which is the inner loop is the child of the parent outer loop
# It works like:
# 1. First itteration of outer loop is 0
# 2. Inner loop first itteration is 0
# 3. Inner loop second and third itteration are 1 and 2
# 4. Then the inner loop ittration stops since its done and goes out
# 5. The Second Irritation of outer loop is 1
# 6. Goes to inner loop and irritate 3 times
# Finally: This process goes until the range is finished


for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")  # The output will be Cordinate

'''
Output:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(4, 0)
(4, 1)
(4, 2)
'''
