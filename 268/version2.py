from typing import List  # Import List type

# Time: O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Compute the expected sum of numbers from 0 to n 
        # Subtract the actual sum and return the difference
        return sum(range(len(nums) +1)) - sum(nums)

# Example usage
solution = Solution()
nums = [3, 0, 1]  # Input list with one missing number
result = solution.missingNumber(nums)
print(result)  # Output: 2
