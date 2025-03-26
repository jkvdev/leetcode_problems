from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)  # Count occurrences of each number
        
        # Custom sorting function:
        # - Primary: Sort by frequency (ascending)
        # - Secondary: Sort by value (descending) for equal frequencies
        def custom_sort(n):
            return (count[n], -n)
        
        nums.sort(key=custom_sort)  # Sort using the custom function
        return nums

# Example usage
solution = Solution()
nums = [4, 1, 1, 2, 2, 2, 3, 3, 3]
print(solution.frequencySort(nums))  
# Output: [4, 1, 1, 3, 3, 3, 2, 2, 2]
