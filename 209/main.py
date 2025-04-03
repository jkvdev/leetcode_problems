
from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
          l = 0  # Left pointer of the sliding window
          total = 0  # Variable to keep track of the sum of the current window
          res = float('inf')  # Initialize result with infinity (to find the minimum)

          # Iterate through the array using the right pointer `r`
          for r in range(len(nums)):
              total += nums[r]  # Add the current element to the window sum

              # Shrink the window from the left while the sum is at least `target`
              while total >= target:
                  # Update the minimum length of a valid sub-array
                  res = min(res, r - l + 1)

                  # Remove the leftmost element from the window and move `l` to the right
                  total -= nums[l]
                  l += 1  # Move the left pointer to reduce the window size

          # If no valid sub-array was found, return 0; otherwise, return the minimum length
          return 0 if res == float('inf') else res
      
      
# Example test case
solution = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
result = solution.minSubArrayLen(target, nums)
print(result)  # Output: 2 (smallest sub-array [4,3] meets the target)