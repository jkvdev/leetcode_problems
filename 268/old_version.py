from typing import List  # Import List type

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # Get the size of the list
        s = set(nums)  # Convert the list to a set for O(1) lookup
        
        for num in range(n + 1):  # Iterate over possible numbers from 0 to n
            if num not in s:  # Check if a number is missing
                return num  # Return the missing number

# Example usage
solution = Solution()
nums = [3, 0, 1]  # Input list with one missing number
result = solution.missingNumber(nums)
print(result)  # Output: 2
