
from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # Get the number of rows and columns in the grid.
        rows, cols = len(grid), len(grid[0])
        
        # Create a list of tuples (query value, original index) for later result assignment.
        q = [(n, i) for i, n in enumerate(queries)]
        # Sort the queries in ascending order, this allows us to process the smallest ones first.
        q.sort()

        # Initialize a min-heap with the top-left cell of the grid (grid[0][0]).
        min_heap = [(grid[0][0], 0, 0)]  # The heap will store tuples of the form (value, row, column)
        # A set to keep track of which cells have been visited to avoid revisiting.
        visit = set([(0, 0)])
        # Initialize the result list. It will store the answers corresponding to each query.
        res = [0] * len(queries)
        # Points will store how many cells are less than the current query value.
        points = 0

        # Iterate over each query value in sorted order
        for limit, index in q:
            # For each query, we process cells in the min-heap
            # We pop from the heap as long as the smallest element in the heap is smaller than the query
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)  # Pop the smallest element from the heap
                points += 1  # This cell is less than the current query, so increment points
                # Check the 4 neighbors (up, down, left, right) of the current cell (r, c)
                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                
                # For each neighbor, if it's within the grid bounds and hasn't been visited, add it to the heap
                for nr, nc in neighbors:
                    if (
                        0 <= nr < rows and 0 <= nc < cols and  # Check grid bounds
                        (nr, nc) not in visit  # Make sure the cell hasn't been visited
                    ):
                        heappush(min_heap, (grid[nr][nc], nr, nc))  # Push the neighbor into the heap
                        visit.add((nr, nc))  # Mark the neighbor as visited

            # Once all points less than the query value are processed, store the result at the correct index
            res[index] = points
        
        # After processing all queries, return the result list containing the answers
        return res
            

# Example Usage
grid = [
    [1, 3, 1],
    [3, 3, 3],
    [3, 3, 1]
]
queries = [3, 4, 1, 2]
solution = Solution()
result = solution.maxPoints(grid, queries)
print(result)  # This will print the result list
