
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort nums and create a dictionary to store the count of smaller numbers
        temp = sorted(nums)  
        d = {}

        # Store the first occurrence index of each number in the sorted list
        for i, num in enumerate(temp):  
            if num not in d:
                d[num] = i  # The index in sorted order represents the count of smaller numbers

        # Replace each number in nums with the number of smaller elements
        return [d[num] for num in nums]
    
# Example run
solution = Solution()
nums = [8, 1, 2, 2, 3]
print(solution.smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]