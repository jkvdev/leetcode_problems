
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get number of rows and columns
        row, col = len(grid), len(grid[0])
        
        # DFS search function
        def dfs(i, j):
            # check edge cases
            # check if out of bounds
            # and if the grid is at a 1
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != "1":
                return
            else: 
                # change the value to 0 to not check again
                grid[i][j] = "0"
                
                # go over the positions around the grid point
                dfs(i, j+1) # right
                dfs(i+1, j) # down
                dfs(i, j-1) # left
                dfs(i-1, j) # up
            
        
        # Initialize number of islands
        num_islands = 0
        
        # Go over the whole grid
        for i in range(row):
            for j in range(col):
                # if the item on a grid is a 1
                if grid[i][j] == "1":
                    # increment number of islands
                    num_islands += 1
                    # do a dfs search
                    dfs(i, j)
                    
        # return result
        return num_islands # Time: O(row*col) Space: O(row*col)
      

# Example Usage
solution = Solution()

# Sample input grid with islands represented by "1" and water by "0"
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# Calling the numIslands method
result = solution.numIslands(grid)

# Printing the result
print(f"Number of islands: {result}")  # Output should be 3