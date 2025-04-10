
from collections import defaultdict
import heapq
from typing import List

# Time: O(K * E)
# Space: O(N)

# Similar approach to Dijkstra's algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a graph (adjacency list) where each node points to its neighbors with associated cost
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p  # There is a flight from node a to node b with price p

        # Priority queue (min-heap) that holds tuples of the form:
        # (current_total_price, current_city, stops_remaining)
        heap = [(0, src, k + 1)]

        # Dictionary to keep track of the maximum stops remaining when visiting a city
        visited = dict()

        # Start processing nodes in the heap
        while heap:
            price, city, stops_left = heapq.heappop(heap)  # Always process the cheapest option next

            # If we reached our destination, return the total price so far
            if city == dst:
                return price

            # If we've visited this city with equal or more stops left before, skip it to avoid reprocessing
            if city in visited and visited[city] >= stops_left:
                continue

            # Update visited dictionary with the current city and stops left
            visited[city] = stops_left

            # If we still have remaining stops, explore neighbors
            if stops_left > 0:
                for nei in f[city]:
                    # Calculate new cost to reach the neighbor
                    new_cost = price + f[city][nei]
                    # Add neighbor to the heap with updated cost and one fewer stop left
                    heapq.heappush(heap, (new_cost, nei, stops_left - 1))

        # If we never reach the destination, return -1
        return -1
      
      
# Example input
n = 4  # Number of cities
flights = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 3, 100],
    [0, 3, 500]
]
src = 0
dst = 3
k = 1

# Run the code
solution = Solution()
cheapest_price = solution.findCheapestPrice(n, flights, src, dst, k)
print("Cheapest price:", cheapest_price)  # Output should be 500