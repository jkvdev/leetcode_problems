from typing import List

# Find Duplicates in an Array
# leetCode: 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set() # HashSet to track seen numbers
        
        for num in nums:
            if num in h:
                return True # Duplicate found
            h.add(num) # Add the number to the HashSet 
            
        return False # No duplicates found
    
sol = Solution()  # Create an instance of Solution

nums1 = [1, 2, 3, 4]  # Example without duplicates
nums2 = [1, 2, 3, 1]  # Example with duplicates

print(sol.containsDuplicate(nums1))  # Output: False
print(sol.containsDuplicate(nums2))  # Output: True
