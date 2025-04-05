
from queue import Queue

# Function to reverse the first k elements of a Queue
def reverseQueueFirstKElements(k, Queue):
    stack = []

    # Step 1: Put the first k elements into a stack (to reverse them)
    for i in range(k):
        stack.append(Queue.get())

    # Step 2: Enqueue back the stack elements (now reversed)
    while stack:
        Queue.put(stack.pop())

    # Step 3: Move the remaining elements (n - k) to the back of the queue
    size = Queue.qsize()
    for i in range(size - k):
        Queue.put(Queue.get())

    return Queue


# Example usage:
q = Queue()
for i in [1, 2, 3, 4, 5]:
    q.put(i)

k = 3

# Call the function
result = reverseQueueFirstKElements(k, q)

# Print the resulting queue
while not result.empty():
    print(result.get(), end=' ')  # Output: 3 2 1 4 5