
from typing import List

# LeetCode 977
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      # Create 2 pointers for the left and right ends of the list
      left, right = 0, len(nums) - 1
      # Initialize an array to store the result
      result = []
      
      # Iterate through the list while the left pointer is less than or equal to the right pointer
      while left <= right:
          # Compare the absolute values of the left and right pointers
          if abs(nums[left]) > abs(nums[right]):
              # Append the square of the left pointer to the result array
              result.append(nums[left] ** 2)
              # Move the left pointer inwards
              left += 1
          else:
              # Append the square of the right pointer to the result array
              result.append(nums[right] ** 2)
              # Move the right pointer inwards
              right -= 1
              
      # Return the result array in reverse
      return result[::-1]
    
# Create an instance of the Solution class
sol = Solution()

# Define input list
nums = [-4, -1, 0, 3, 10]

# Call the function and print the result
print(sol.sortedSquares(nums))