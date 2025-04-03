
from typing import List

# Time: O(n) every time
# Space: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums # Store the input array

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1]) # Calculate sum from left to right (inclusive)


# Example Usage
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)  # Create an instance of NumArray

# Get sum of elements from index 0 to 2
print(obj.sumRange(0, 2))  # Output: 1  (i.e., -2 + 0 + 3 = 1)

# Get sum of elements from index 2 to 5
print(obj.sumRange(2, 5))  # Output: -1  (i.e., 3 + (-5) + 2 + (-1) = -1)