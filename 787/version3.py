

from typing import List

# Time: O(K * E)
# Space: O(N)

# Bellman Ford Algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize a list of prices with infinity for all cities
        prices = [float('inf')] * n
        prices[src] = 0  # The cost to reach the source city from itself is 0

        # Repeat the process for up to k stops (k+1 total levels)
        for i in range(k + 1):
            tmpPrices = prices.copy()  # Copy current prices to avoid updating in-place

            for s, d, p in flights: # loop through source, destination and price for each flight
                # If the source city is not yet reachable, skip it
                if prices[s] == float('inf'):
                    continue

                # Relax the edge if a cheaper path is found
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices  # Update the main prices list

        # If the destination city is still unreachable, return -1
        return -1 if prices[dst] == float('inf') else prices[dst]  # Return the cheapest cost to the destination
      
      
      
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
k = 2

# Run the code
solution = Solution()
cheapest_price = solution.findCheapestPrice(n, flights, src, dst, k)
print("Cheapest price:", cheapest_price)  # Output should be 300