
from typing import List

# Time: O(n log n)
# Space: O(n)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
      # Step 1: Sort array
      arr.sort()
      
      # Step 2: Find minimum absolute difference
      min_diff = float('inf')
      for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i -1])
        
      # Step 3: Collect all pairs with the minimum difference
      res = []
      for i in range(1, len(arr)):
        if arr[i] - arr[i -1] == min_diff:
          res.append([arr[i -1], arr[i]])
          
      return res
    
    
# Example usage:
solution = Solution()
arr = [4, 2, 1, 3]
output = solution.minimumAbsDifference(arr)
print(output)  # Expected Output: [[1, 2], [2, 3], [3, 4]]