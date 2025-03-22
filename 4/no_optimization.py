# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

# Solution class
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        # return the median based on the length of the merged array
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]
          
          
# Test cases
sol = Solution()

# Example 1
nums1 = [1, 3]
nums2 = [2]
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.5

# Example 3
nums1 = [0, 0]
nums2 = [0, 0]
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 0.0

# Example 4
nums1 = []
nums2 = [1]
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 1.0

# Example 5
nums1 = [2]
nums2 = []
print(sol.findMedianSortedArrays(nums1, nums2))  # Output: 2.0
