
from typing import List

# Time: O(n)
# Time: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # Create an empty set to store unique numbers in the current window
        
        # Iterate through the list while keeping track of the index (i) and value (num)
        for i, num in enumerate(nums):
            if num in seen:  # If num is already in the set, we found a duplicate within range k
                return True  # Return True immediately
            
            seen.add(num)  # Add the current number to the set
            
            # If the window size exceeds k, remove the oldest element (nums[i - k])
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False  # If no nearby duplicate is found, return False
    
    
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