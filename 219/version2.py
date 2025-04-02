
from typing import List

# Time: O(n)
# Time: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number in the list
        seen = {}
        
        # Loop through the list of numbers along with their index
        for i, num in enumerate(nums):
            # Check if the current number has been seen before
            # and if the difference between the current index and the last seen index is <= k
            if num in seen and i - seen[num] <= k:
                # If a nearby duplicate is found, return True
                return True
            
            # Update the dictionary with the current index of the number
            seen[num] = i
        
        # If no nearby duplicates are found, return False
        return False
    
    
# Example test cases
solution = Solution()

nums1 = [1, 2, 3, 1]
k1 = 3
print(solution.containsNearbyDuplicate(nums1, k1))  # Output: True (1 appears twice within 3 indices)

nums2 = [1, 2, 3, 4, 5]
k2 = 2
print(solution.containsNearbyDuplicate(nums2, k2))  # Output: False (No duplicates within k distance)

nums3 = [1, 2, 3, 1, 2, 3]
k3 = 2
print(solution.containsNearbyDuplicate(nums3, k3))  # Output: False (Duplicates exist but are not within k distance)