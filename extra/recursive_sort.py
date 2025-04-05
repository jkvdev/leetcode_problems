
# Extra Exercise:
# Sort a stack

from typing import List

# Time: O(n^2)
# Space: O(n)
class Solution:
    def sortStack(self, stack: List[int]) -> List[int]:
        # Helper function that recursively sorts the stack
        def sortStack(stack):
            # Base case: if the stack is empty, we don't need to do anything
            if len(stack) == 0:
                return stack
            
            # Pop the top element from the stack
            top = stack.pop()
            # Recursively sort the remaining elements in the stack
            sortStack(stack)
            # Insert the popped element in sorted order in the stack
            inSortedOrder(stack, top)
        
        # Helper function that inserts a value into the stack while maintaining sorted order
        def inSortedOrder(stack, value):
            # Base case: if the stack is empty or the value to be inserted is greater than or equal to the top value, just add it
            if len(stack) == 0 or stack[-1] <= value:
                stack.append(value)
                return
            
            # Pop the top element, as it is larger than the value we want to insert
            top = stack.pop()
            # Recursively call inSortedOrder to continue placing the value in the correct position
            inSortedOrder(stack, value)
            # Push the previously popped element back into the stack after the insertion of the value
            stack.append(top)
        
        # Start the sorting process by calling sortStack
        sortStack(stack)
        # Return the sorted stack
        return stack
        
        
        
# Create an instance of Solution
sol = Solution()

# Test the method with an unsorted stack
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sol.sortStack(stack)

# Print the sorted stack
print(sorted_stack)