
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the matrix
        rows, cols = len(heights), len(heights[0])
        
        # Sets to track the cells that can flow to the Pacific and Atlantic oceans
        pac, atl = set(), set()
        
        # Depth-first search (DFS) function to explore reachable cells
        def dfs(r, c, visit, prevHeight):
            """
            Recursively visits cells that can flow into a given ocean.
            
            Parameters:
            - r, c: Current row and column position
            - visit: The set tracking visited positions for an ocean
            - prevHeight: Height of the previous cell (to ensure water flows downhill or remains level)
            """
            
            # If the cell is already visited OR out of bounds OR water can't flow there, return
            if ((r, c) in visit or # Already visited
              r < 0 or c < 0 or r == rows or c == cols or # Out of bounds 
              heights[r][c] < prevHeight): # Water cannot flow uphill
                  return
                
            # Mark the cell as visited for the given ocean
            visit.add((r, c))
            
            # Explore all four possible directions (down, right, up, left)
            dfs(r + 1, c, visit, heights[r][c]) # Move down
            dfs(r, c + 1, visit, heights[r][c]) # Move right
            dfs(r - 1, c, visit, heights[r][c]) # Move up
            dfs(r, c - 1, visit, heights[r][c]) # Move left
        
        # Start DFS from the first and last row 
        # (to mark Pacific and Atlantic flows)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # Top row (flows to Pacific Ocean)
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # Bottom row (flows to Atlantic Ocean)
            
        # Start DFS from the first and last column 
        # (to mark Pacific and Atlantic flows)
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # Left column (flows to Pacific Ocean)
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # Right column (flows to Atlantic Ocean)
            
        # Find cells that can reach both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c]) # If a cell is in both sets, add it to the result
                    
        return res # Return the list of valid coordinates
      
      
      
# Example input: Heights of a 5x5 grid
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

# Create an instance of Solution
sol = Solution()

# Run the function and print the output
print(sol.pacificAtlantic(heights))