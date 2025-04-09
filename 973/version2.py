
import heapq
from typing import List

# Time: O(n log k)
# Space: O(k)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []   # Initialize an empty heap.
                    # We'll use it as a max-heap by storing negative distances.

        # Iterate over each point (x, y) in the list of points
        for (x, y) in points:
            # Calculate the negative squared Euclidean distance from the origin (0, 0).
            # We use negative values so that the largest distance appears at the top of the min-heap,
            # effectively turning it into a max-heap.
            dist = -(x * x + y * y)

            if len(heap) == k:
                # If the heap already contains k points:
                # Compare the new point's distance to the current farthest point (which is at heap[0]).
                if dist > heap[0][0]:
                    # If the new point is closer than the farthest one in the heap:
                    # Replace the farthest with the current point to maintain only the k closest.
                    heapq.heapreplace(heap, (dist, x, y))
            else:
                # If the heap has fewer than k points, just add the current point.
                heapq.heappush(heap, (dist, x, y))

        # Once all points have been processed, extract just the (x, y) coordinates
        # from the heap and return them as the final result.
        return [(x, y) for (dist, x, y) in heap]
    
    
    
# Example usage:
solution = Solution()
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(solution.kClosest(points, k))  # Output: [[-2, 2], [0, 1]]