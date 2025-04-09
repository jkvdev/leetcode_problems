
import heapq
from typing import List

# Time: O(n log k)
# Space: O(k)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # This will be our max-heap (using negative distances)

        # Loop through each point in the input list
        for (x, y) in points:
            # Calculate the squared Euclidean distance from the origin (0, 0)
            # We use negative distance because Python's heapq is a min-heap by default.
            dist = -(x*x + y*y)

            # If we already have k elements in the heap, push and pop in one step.
            # This maintains the size of the heap to exactly k.
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                # If we have fewer than k elements, just push the new point
                heapq.heappush(heap, (dist, x, y))

        # Extract the x and y values from the heap elements and return the final list
        # Each element in the heap is a tuple: (negative_distance, x, y)
        return [(x, y) for (dist, x, y) in heap]
    
    
    
# Example usage:
solution = Solution()
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(solution.kClosest(points, k))  # Output: [[-2, 2], [0, 1]]