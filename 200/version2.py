
from typing import List
from collections import deque

# Time: O(n*m)
# Space: O(n*m)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, return 0 (no islands)
        if not grid:
            return 0

        # Helper function to perform BFS to traverse an entire island
        def bfs(r, c):
            q = deque()  # Initialize a queue for BFS
            visit.add((r, c))  # Mark the current cell as visited
            q.append((r, c))  # Enqueue the starting position

            while q:  # Process all nodes in the queue
                row, col = q.popleft()  # Dequeue the current cell
                # Define four possible directions (up, down, left, right)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:  # Check all 4 directions
                    nr, nc = row + dr, col + dc  # Compute new row & column

                    # Check if the new position is within grid boundaries,
                    # is land ('1'), and hasn't been visited yet
                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == '1' and (nr, nc) not in visit):
                        q.append((nr, nc))  # Enqueue the valid land cell
                        visit.add((nr, nc))  # Mark it as visited

        count = 0  # Variable to store the number of islands
        rows, cols = len(grid), len(grid[0])  # Get grid dimensions
        visit = set()  # Set to track visited land cells

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ('1') and hasn't been visited, start a BFS
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)  # Perform BFS from this land cell
                    count += 1  # Increase island count since we found one

        return count  # Return the total number of islands
        

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