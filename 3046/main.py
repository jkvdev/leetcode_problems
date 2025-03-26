
from typing import List
from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)  # Count occurrences of each number
        
        # Check if any number appears more than twice
        for freq in counter.values():
            if freq > 2:
                return False

        return True
      
      
# Example usage
solution = Solution()
nums = [1, 2, 3, 4, 1, 2, 3, 4]  # This should return True (all elements appear at most twice)
print(solution.isPossibleToSplit(nums))  # Output: True

nums2 = [1, 1, 1, 2, 2, 3, 3]  # This should return False (1 appears more than twice)
print(solution.isPossibleToSplit(nums2))  # Output: False