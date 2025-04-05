
from collections import deque

# Time: O(n)
# Space: O(n)
class MyStack:
    def __init__(self):
        # Initialize an empty deque to hold the elements
        self.queue = deque()

    def push(self, x: int) -> None:
        # Append element to the deque
        self.queue.append(x)

    def pop(self) -> int:
        # Pop elements one by one from the front of the queue until only the last element remains
        for i in range(len(self.queue) - 1):
            # Move elements from front of the queue to back to maintain stack behavior
            self.push(self.queue.popleft())
        
        # Pop and return the last element, which is the top of the stack
        return self.queue.popleft()

    def top(self) -> int:
        # Return the last element in the deque without removing it
        return self.queue[-1]

    def empty(self) -> bool:
        # Check if the deque is empty
        return len(self.queue) == 0
    

# Example usage:
stack = MyStack()

# Push some values onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Check the top value of the stack
print(stack.top())  # Output: 3

# Pop a value from the stack
print(stack.pop())  # Output: 3

# Check the top value again after popping
print(stack.top())  # Output: 2

# Check if the stack is empty
print(stack.empty())  # Output: False

# Pop the remaining values
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

# Check if the stack is empty now
print(stack.empty())  # Output: True