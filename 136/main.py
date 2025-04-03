from typing import List  # Import List type hint

# Find the number that doesn't repeat
# All the numbers show twice except one
# Can use an XOR operation which nullifies 
# the repeating numbers (bit by bit)
# Example: if they are the same they turn to 0
# 1010 ^ (XOR) 1010 => 0000
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for n in nums:
            res = res ^ n # XOR operation
        return res
        
# Create an instance of the Solution class
sol = Solution()

# Test the function with an example input
nums = [4, 1, 2, 1, 2]  # Example input where 4 appears once
result = sol.singleNumber(nums)

# Print the result
print(f"The single number is: {result}")