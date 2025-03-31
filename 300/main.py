
from typing import List

# Time: O(n**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create an array 'lis' where each element is initialized to 1.
        # 'lis[i]' represents the length of the longest increasing subsequence ending at index 'i'.
        lis = [1] * len(nums)

        # Iterate over the array in reverse order (starting from the second last element)
        for i in range(len(nums) - 1, -1, -1):
            # Check elements ahead of 'i' to find increasing sequences
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:  # If nums[i] is smaller, it can be part of an increasing subsequence
                    # Update 'lis[i]' to store the maximum LIS length found so far
                    lis[i] = max(lis[i], 1 + lis[j])

        # The longest increasing subsequence is the maximum value in the 'lis' array
        return max(lis)
    

# Create an instance of Solution
solution = Solution()

# Example test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = solution.lengthOfLIS(nums)

# Print result
print(result)  # Output: 4 (The longest increasing subsequence is [2, 3, 7, 101])