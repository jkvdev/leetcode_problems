from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set() # Set to track the columns where queens are placed
        posDiag = set() # Set to track positive diagonals (r + c)
        negDiag = set() # Set to track negative diagonals (r - c)
        
        res = [] # This will store all the valid board configurations
        board = [["."] * n for i in range(n)] # Initialize an empty board with '.' (representing empty spaces)
        
        # Backtracking row by row
        def backtrack(r):
            # If all queens have been placed on the board
            if r == n:
                copy = ["".join(row) for row in board] # Convert the board rows to strings and add to the result
                res.append(copy)
                return 
            
            # Loop over column positions
            for c in range(n):
                # Skip if the column or diagonal is already occupied
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue 
                
                col.add(c) # Mark the column as occupied
                posDiag.add(r + c) # Mark the positive diagonal as occupied
                negDiag.add(r - c) # Mark the negative diagonal as occupied
                board[r][c] = "Q" # Place a queen at position (r, c)
                
                backtrack(r + 1) # Move to the next row and continue placing queens
                
                col.remove(c) # Unmark the column as occupied
                posDiag.remove(r + c) # Unmark the positive diagonal as occupied
                negDiag.remove(r - c) # Unmark the negative diagonal as occupied
                board[r][c] = "." # Remove the queen from the board
        
        backtrack(0) # begin back tracking from the first row
        return res # Return all valid board configurations
        
        
# Test with n = 4
sol = Solution()
solutions = sol.solveNQueens(4)

# Print all valid solutions
for i, board in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in board:
        print(row)
    print()