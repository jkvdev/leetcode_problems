from typing import List

# Majority Element
# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      candidate = None
      count = 0
      
      for num in nums:
        if count == 0:
          candidate = num
          
        count += 1 if num == candidate else -1
        
      return candidate
    
sol = Solution()  # Create an instance of Solution
nums = [3, 2, 3]  # Example input
result = sol.majorityElement(nums)  # Call the function
print(result)  # Output: 3
