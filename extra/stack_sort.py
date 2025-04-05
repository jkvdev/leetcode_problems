
# Extra Exercise:
# Sort a stack

from typing import List

# Time: O(n^2)
# Space: O(n)
class Solution:
    def sortStack(self, stack: List[int]) -> List[int]:
        temp = []
        
        while stack:
            num = stack.pop()
            
            # Move elements from temp to stack to maintain sorted order
            while temp and temp[-1] > num:
                stack.append(temp.pop())
            
            # Append the number to the temporary stack
            temp.append(num)
        
        # Return the sorted stack
        return temp

# Create an instance of Solution
sol = Solution()

# Test the method with an unsorted stack
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sol.sortStack(stack)

# Print the sorted stack
print(sorted_stack)