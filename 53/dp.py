from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
# leetCode: 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
          # Create a DP array where dp[i] represents the 
          # maximum sub-array sum ending at index i
          dp = [0] * len(nums)
          
          # Iterate through the input array while 
          # keeping track of the maximum sum sub-array
          for i, n in enumerate(nums):
              # The maximum sum ending at index i is either:
              # 1. The current number itself (starting a new sub-array)
              # 2. The sum of the current number and 
              # the maximum sub-array sum ending at i-1
              dp[i] = max(n, dp[i - 1] + n)
          
          # The maximum sub-array sum is 
          # the largest value in the dp array
          return max(dp)
    
# Example Usage:
sol = Solution()

print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6 (sub-array [4,-1,2,1])
print(sol.maxSubArray([1]))  # Output: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23