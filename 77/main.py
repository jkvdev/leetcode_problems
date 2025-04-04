
from typing import List

# Time: O(k * (n! / ( (n - k)! * k!) ) ) OR 
# O(k * ( n choose k ) ) -> Binomial coefficient
# Space: O(k)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      # Helper function using backtracking
        def backtrack(start, path):
            # If the current combination has k elements, it's complete
            if len(path) == k:
                result.append(path[:])  # Add a **copy** of the current path to result
                return  # Backtrack

            # Iterate through the numbers from 'start' to 'n'
            for i in range(start, n + 1):
                path.append(i)            # Choose the current number
                backtrack(i + 1, path)    # Move to the next number
                path.pop()                # Undo the choice (backtrack) and try the next one

        result = []               # This will hold all the valid combinations
        backtrack(1, [])          # Start the backtracking with 1 and an empty path
        return result             # Return the list of combinations
    
    
# Example usage
sol = Solution()
output = sol.combine(4, 2)  # All combinations of 2 numbers out of 1..4
print("Combinations:", output)