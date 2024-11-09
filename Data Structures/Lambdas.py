items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 20),
]


# def sort_item(item):
#     return item[1]

# Lambda is a simple, one line anonymous function that we can pass to other functions
# Lambda syntax ----> lambda parameters : expression
# This one line is equal to out function sort_item

items.sort(key=lambda item: item[1])
print(items)
