
import heapq
from typing import List

# Time: O(n log k)
# Space: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      # Use heapq.nlargest to get the k largest elements, 
      # and return the last one (i.e. kth largest)
      return heapq.nlargest(k, nums)[-1]
    
    
# Example usage
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2

result = sol.findKthLargest(nums, k)
print(f"The {k}th largest element is:", result)