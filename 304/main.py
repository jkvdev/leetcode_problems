
from typing import List

# Time: O(n^2)
# Space: O(n^2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Get number of rows and columns in the original matrix
        rows, cols = len(matrix), len(matrix[0])
        # Initialize a prefix sum matrix (extra row and column filled with zeros for easier math)
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Fill the prefix sum matrix
        for r in range(rows):
            prefix = 0  # Prefix sum for the current row
            
            for c in range(cols):
                prefix += matrix[r][c]  # Add current element to row prefix sum
                above = self.sumMat[r][c + 1]  # Get the value from the row above at the same column
                # Store the cumulative sum up to this point (including above rows and current row's prefix)
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Offset all indices by 1 to align with sumMat indexing
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        # Use inclusion-exclusion principle to compute the sum of the sub-matrix
        bottomRight = self.sumMat[r2][c2]        # Total area from (0,0) to (row2, col2)
        above = self.sumMat[r1 - 1][c2]          # Subtract area above the desired sub-matrix
        left = self.sumMat[r2][c1 - 1]           # Subtract area to the left of the desired sub-matrix
        topLeft = self.sumMat[r1 - 1][c1 - 1]    # Add back the overlapping top-left area

        # Final result is the sum of elements in the region (row1, col1) to (row2, col2)
        return bottomRight - above - left + topLeft

# Example usage:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

num_matrix = NumMatrix(matrix)

# Query the sum of the rectangle from (2, 1) to (4, 3)
print(num_matrix.sumRegion(2, 1, 4, 3))  # Output should be 8


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)