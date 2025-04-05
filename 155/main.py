
# Time: O(1)
# Space: O(n)
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Determine new min val
        if not self.stack: 
            current_min = val # if stack is empty, the val is min
        else:
            # check min val for each created val
            current_min = min(val, self.stack[-1][1])
        # save val and min val as tuple to avoid looping
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
      return self.stack[-1][1]



# Create an instance of MinStack
min_stack = MinStack()

# Push elements onto the stack
min_stack.push(5)
min_stack.push(3)
min_stack.push(8)
min_stack.push(2)

# Get the current minimum value
print(min_stack.getMin())  # Output: 2

# Get the top element of the stack
print(min_stack.top())  # Output: 2

# Pop the top element
min_stack.pop()

# Get the current minimum value after popping
print(min_stack.getMin())  # Output: 3

# Get the top element after popping
print(min_stack.top())  # Output: 8
