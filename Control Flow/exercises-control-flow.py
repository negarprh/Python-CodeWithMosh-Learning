# A program that display even numbers between 1 to 10
# And print how many even numbers there are

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)

print(f"we have {count} even numbers between 1 to 10")
