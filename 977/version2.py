
from typing import List

# LeetCode 977
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      n = len(nums) # Get the length of the input array
      res = [0] * n   # Create an empty result array of size n
      l, r = 0, n - 1   # Left pointer (start), Right pointer (end)
      
      for i in range(n - 1, -1, -1): # Iterate from last index to 0
          if abs(nums[l]) > abs(nums[r]): # Compare the absolute values of the left and right pointers
              res[i] = nums[l] ** 2
              l += 1 # Move left pointer forward
          else:
              res[i] = nums[r] ** 2
              r -= 1 # Move right pointer backward
              
      return res
    
# Create an instance of the Solution class
sol = Solution()

# Define input list
nums = [-4, -1, 0, 3, 10]

# Call the function and print the result
print(sol.sortedSquares(nums))