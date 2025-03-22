# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

# Solution class
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # determine the length of the arrays
        total_len = len(nums1) + len(nums2)
        # find the midpoint and round it down to the nearest integer
        half_len = total_len // 2
        
        # define left and right values
        left = 0
        right = len(nums1)

        # loop through the array as long as left is less than or equal to right
        while left <= right:
            # find the partition index for nums1
            partition1 = (left + right) // 2
            # find the partition index for nums2
            partition2 = half_len - partition1
            
            # find the left and right values for both partitions
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == len(nums1) else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            # Debugging: Print partition values
            # print(f"partition1: {partition1}, partition2: {partition2}")
            # print(f"max_left1: {max_left1}, min_right1: {min_right1}")
            # print(f"max_left2: {max_left2}, min_right2: {min_right2}")

            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is even, take the average of the max left and min right
                if total_len % 2 == 0:
                    median = (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                # If total length is odd, take the max of the left partition
                else:
                    median = min(min_right1, min_right2)

                # return the median
                return median
            elif max_left1 > min_right2:
                # If maxLeftX is greater than minRightY, move left
                right = partition1 - 1
            else:
                # If maxLeftY is greater than minRightX, move right
                left = partition1 + 1

          
          
          
# Test cases
sol = Solution()

print(sol.findMedianSortedArrays([1, 3], [2]))          # Output: 2.0
print(sol.findMedianSortedArrays([1, 2], [3, 4]))       # Output: 2.5
print(sol.findMedianSortedArrays([0, 0], [0, 0]))       # Output: 0.0
print(sol.findMedianSortedArrays([], [1]))              # Output: 1.0
print(sol.findMedianSortedArrays([2], []))              # Output: 2.0
print(sol.findMedianSortedArrays([1, 2], [1, 2]))       # Output: 1.5
