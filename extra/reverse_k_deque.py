
from collections import deque

# Time: O(n)
# Space: O(k)

# Function to reverse the first k elements of a Queue
def reverse_first_k_elements(k, q):
  stack = []
  
  # put the first k elements in a stack
  for i in range(k):
    stack.append(q.popleft())
    
  # push the contents of the stack to the back of the queue
  # will be added in reverse due to stack LIFO
  while stack: 
    q.append(stack.pop())
    
  # pop and push elements in queue
  # that should come after first k elements in queue
  for i in range(len(q) -k):
    q.append(q.popleft())
    
  return q

# Example usage:
queue = deque([1, 2, 3, 4, 5])
k = 3

# Call the function
result = reverse_first_k_elements(k, queue)

# Print the modified queue
print(list(result))  # Output: [3, 2, 1, 4, 5]