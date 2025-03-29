
from typing import List

# Time: O(log n)
# Space: O(1)

# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize the left and right pointers
        
        # Loop to perform binary search
        while l <= r:
            mid = (l + r) // 2  # Find the middle index of the current search space
            if target == nums[mid]:
                return mid  # If the target is found, return the index of the target
            
            # Left sorted portion
            if nums[l] <= nums[mid]:  # Check if the left portion is sorted
                # If the target is in the left sorted portion, adjust the right pointer
                # If target is greater than mid or less than left, search right portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # Search in the right portion
                else:
                    r = mid - 1  # Search in the left portion
            # Right sorted portion
            else:  # If the right portion is sorted
                # If the target is in the right sorted portion, adjust the left pointer
                # If target is less than mid or greater than right, search left portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # Search in the left portion
                else:
                    l = mid + 1  # Search in the right portion

        return -1  # If the target is not found, return -1
      

# Example rotated sorted array
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Create a Solution object
sol = Solution()

# Call the search function and print result
result = sol.search(nums, target)
print(f"Index of {target}: {result}")  # Expected Output: 4