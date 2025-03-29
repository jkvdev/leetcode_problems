from typing import List
from collections import deque

# Time: O(m*n)
# Space: O(m*n)

# Breadth-First Search (BFS).
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Define constants for different states of the grid
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid
        
        num_fresh = 0  # Count the number of fresh oranges
        que = deque()  # Initialize a queue to perform BFS

        # Step 1: Identify all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:  # If the cell has a rotten orange
                    que.append((i, j))  # Add its coordinates to the queue
                elif grid[i][j] == FRESH:  # If the cell has a fresh orange
                    num_fresh += 1  # Increase fresh orange count
        
        # If there are no fresh oranges, return 0 (no time needed)
        if num_fresh == 0:
            return 0
        
        num_minutes = -1  # Initialize time counter (set to -1 since we start at minute 0)

        # Step 2: Perform BFS to rot adjacent fresh oranges
        while que:
            que_size = len(que)  # Get the number of rotten oranges at the current level
            num_minutes += 1  # Increase minute count
            
            # Process all rotten oranges for this minute
            for _ in range(que_size):
                i, j = que.popleft()  # Get the current rotten orange
                
                # Check all four possible directions (right, down, left, up)
                for r, c in [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]:
                    # Ensure (r, c) is within bounds and contains a fresh orange
                    if (0 <= r < m and 0 <= c < n and grid[r][c] == FRESH):
                        grid[r][c] = ROTTEN  # Mark the fresh orange as rotten
                        num_fresh -= 1  # Reduce fresh orange count
                        que.append((r, c))  # Add newly rotten orange to the queue
        
        # Step 3: Return the result
        # If there are still fresh oranges left, return -1 (some oranges never rotted)
        return num_minutes if num_fresh == 0 else -1
      

# Example Grid: 0 = empty, 1 = fresh, 2 = rotten
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

# Create Solution object
sol = Solution()

# Run the function and print the result
print(sol.orangesRotting(grid))  # Expected output: 4