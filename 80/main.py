
from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1  # Pointer to place the next unique element
        count = 1  # Track how many times we've seen a duplicate
        n = len(nums)  # Length of the input list
        
        for i in range(1, n):  # Start from the second element
            if nums[i] == nums[i-1]:  # If current element is same as previous one
                count += 1
            else:
                count = 1  # Reset count if the element is different
            
            if count <= 2:  # Allow at most two duplicates
                nums[j] = nums[i]  # Place the current element at the next position
                j += 1  # Move the pointer forward
        
        return j  # Return the new length of the list without extra duplicates
      

# Example Usage
solution = Solution()

# Sample input list with duplicates
nums = [1, 1, 1, 2, 2, 3]

# Calling the removeDuplicates method
new_length = solution.removeDuplicates(nums)

# Print the result
print(f"New length: {new_length}")
print(f"Modified list: {nums[:new_length]}")  # Only print the part of the list that was modified