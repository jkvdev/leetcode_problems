
from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0  # Initialize the total time counter
        # Start from the last point in the list (pop removes and returns the last element)
        x1, y1 = points.pop()  

        while points:  # Loop until all points are processed
            x2, y2 = points.pop()  # Get the next point from the list
            # Calculate the Chebyshev distance (max of x and y differences)
            # This is the minimum number of steps required to move diagonally or straight
            res += max(abs(y2 - y1), abs(x2 - x1))  
            # Update x1, y1 to the new point for the next iteration
            x1, y1 = x2, y2  
        
        return res  # Return the total time required
    
    
# Example usage:
solution = Solution()
points = [[1, 1], [3, 4], [-1, 0]]  # Example input
result = solution.minTimeToVisitAllPoints(points)
print(result)  # Expected Output: 7