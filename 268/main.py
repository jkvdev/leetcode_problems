from typing import List  # Import List type

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Get the length of the array
        n = len(nums)  
        
        # Calculate the expected sum of numbers from 0 to n using the formula:
        # Sum of first n natural numbers = n * (n+1) // 2
        expected = n * (n + 1) // 2
        
        # Compute the actual sum of elements present in the given list        
        # The missing number is the difference between the expected and actual sum
        return expected - sum(nums)

# Example usage
solution = Solution()
nums = [3, 0, 1]  # Input list with one missing number
result = solution.missingNumber(nums)
print(result)  # Output: 2
