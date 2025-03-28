
from typing import List  # Required for type hinting

# Time: O(n*m)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        # Dfs search function
        def capture(r, c):
            # edge cases
            if (r < 0 or c < 0 or 
                r == rows or c == cols or 
                board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            
            # Look at adjacent cases
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        
        # 1. (DFS) Capture un-surrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and 
                    (r in [0, rows-1] or c in [0, cols-1])):
                    capture(r, c)
        
        # 2. (Nested loops) Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # 3. (Nested loops) Un-capture un-surrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
              


# Example Input Board
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

# Create an instance of Solution and call the function
sol = Solution()
sol.solve(board)

# Print the modified board
for row in board:
    print(row)