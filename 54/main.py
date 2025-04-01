
from typing import List

# Time: O(m*n)
# Space: O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      ret = []
      
      while matrix:
        # Step 1: add first row/list of matrix
        ret += matrix.pop(0)
        
        # Step 2: append last element of all lists in order
        if matrix and matrix[0]:
          for row in matrix:
            ret.append(row.pop())
            
        # Step 3: add reverse of the last list/row
        if matrix:
          ret += matrix.pop()[::-1]
          
        # Step 4: append first element of all rows/lists in reverse
        if matrix and matrix[0]:
          for row in matrix[::-1]:
            ret.append(row.pop(0))
            
      return ret
    
    
# Test input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create an instance of Solution
sol = Solution()

# Run the function and print the result
print(sol.spiralOrder(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]