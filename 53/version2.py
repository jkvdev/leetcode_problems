from typing import List

# Kadane's Algorithm
# Maximum Subarray Sum
# Time Complexity: O(n)
# Space Complexity: O(1)
# leetCode: 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      curr_sum = 0 # Current sum
      max_sum = nums[0] # Maximum sum
      
      for n in nums:
        if curr_sum < 0: # If the current sum is negative, reset it to 0
          curr_sum = 0
        
        curr_sum += n # Add the current element to the current sum
        max_sum = max(max_sum, curr_sum) # Update the maximum sum
          
      return max_sum
    
# Example Usage:
sol = Solution()

print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6 (subarray [4,-1,2,1])
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23