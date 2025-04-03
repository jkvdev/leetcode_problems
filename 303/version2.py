
from typing import List

# Time: O(n) once then O(1) as it becomes constant
# Space: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        # Create a prefix sum array, initializing with 0 at index 0.
        # This helps in computing sum queries in O(1) time.
        self.acc_nums = [0]  

        # Compute the prefix sum (cumulative sum) for the given array.
        for num in nums:
            # Append the running sum (last element in acc_nums + current num)
            self.acc_nums.append(self.acc_nums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of elements from index 'left' to 'right' (inclusive).
        Instead of summing directly (O(n)), we use the prefix sum approach (O(1)).
        Formula: sumRange(left, right) = acc_nums[right+1] - acc_nums[left]
        """
        return self.acc_nums[right + 1] - self.acc_nums[left]


# Example Usage
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)  # Create an instance of NumArray

# Get sum of elements from index 0 to 2
print(obj.sumRange(0, 2))  # Output: 1  (i.e., -2 + 0 + 3 = 1)

# Get sum of elements from index 2 to 5
print(obj.sumRange(2, 5))  # Output: -1  (i.e., 3 + (-5) + 2 + (-1) = -1)

# Get sum of elements from index 0 to 5
print(obj.sumRange(0, 5))  # Output: -3 (i.e., sum of the entire array)