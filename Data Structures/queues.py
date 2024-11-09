# Queues are another linear data structure
# They are unlike stacks, have the behavior of FIFO
# Which FIFO is ---> First in, First Out
# It is like Queues in real life, when you are in queues in real life, like when you are in queues , first person go first

# But rememeber in large lists it is not very effiecine becuase if we have a list of 1001 items
# if we remove the first item, we need to move another 1000 items by one to the left in memory
# in situations like this, we better to use DEQUEUES objects

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # We dont have this method in list object which means if we dont call it from collection moudale, we can not use it
print(queue)  # Print deque([2, 3])

if not queue:
    print("Empty")
