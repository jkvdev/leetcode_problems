

from typing import List
import bisect  # Importing bisect for binary search operations

# Time: O(n log n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # This list will store the smallest possible ending element of increasing subsequences.
        sub = []  

        # Iterate over each number in the input list
        for num in nums:
            # Perform a binary search to find the first index where `num` can replace an element in `sub`
            idx = bisect.bisect_left(sub, num)
            
            # If `num` is larger than all elements in `sub`, it extends the LIS, so append it.
            if idx == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the element at index `idx` with `num`
                # This ensures `sub` remains as small as possible while maintaining an increasing order.
                sub[idx] = num
        
        # The length of `sub` represents the length of the longest increasing subsequence.
        return len(sub)
    

# Create an instance of Solution
solution = Solution()

# Example test case
nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = solution.lengthOfLIS(nums)

# Print result
print(result)  # Output: 4 (The longest increasing subsequence is [2, 3, 7, 101])