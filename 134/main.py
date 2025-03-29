
from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
          
        total = 0  # Tracks the remaining gas
        start = 0  # Starting index of the circuit

        for i in range(len(gas)):
            total += (gas[i] - cost[i])  # Net gas after reaching next station

            # If total gas is negative, restart at the next station
            if total < 0:
                total = 0
                start = i + 1
        
        return start

# Example usage:
sol = Solution()
gas_stations = [1, 2, 3, 4, 5]
costs = [3, 4, 5, 1, 2]
result = sol.canCompleteCircuit(gas_stations, costs)
print(result)  # Expected output: 3
