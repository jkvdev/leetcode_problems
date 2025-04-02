
from typing import List
import collections

# LeetCode 977
# Time: O(n)
# Space: O(1)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()  # Use deque for efficient insertions at the front
        l, r = 0, len(nums) - 1  # Left and right pointers
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])  # Take absolute values
            if left > right:
                answer.appendleft(left * left)  # Insert at the beginning
                l += 1
            else:
                answer.appendleft(right * right)  # Insert at the beginning
                r -= 1
                
        return list(answer)  # Convert deque to list before returning
    
# Create an instance of the Solution class
sol = Solution()

# Define input list
nums = [-4, -1, 0, 3, 10]

# Call the function and print the result
print(sol.sortedSquares(nums))