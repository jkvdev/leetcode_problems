# Desc: Rotate Image
# Difficulty: Medium    
from typing import List

# TODO: Solve this problem
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                # mirror pointer because it's a square matrix
                top, bottom = l, r 
                
                # save the top left value
                topLeft = matrix[top][l + i]
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move top left into top right
                matrix[top + i][r] = topLeft
                
            # Update pointers
            r -= 1
            l += 1
            

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
sol.rotate(matrix)

# Print rotated matrix
for row in matrix:
    print(row)