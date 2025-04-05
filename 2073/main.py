
from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0  # This will store the total time (in seconds) needed for person at index k to buy all their tickets
        
        # Loop through each person in the queue
        for i in range(len(tickets)):
            if i <= k:
                # If the person is at or before index k, they will have a chance to buy up to tickets[k] tickets
                # This is because they are still in the queue when person k is buying
                result += min(tickets[i], tickets[k])
            else:
                # If the person is after index k, they will only have a chance to buy up to tickets[k] - 1
                # Because after person k buys their last ticket, the process stops and the rest don't get another turn
                result += min(tickets[i], tickets[k] - 1)

        return result  # Return the total time it takes for person at index k to finish buying all their tickets
    
    
# Create an instance of Solution
sol = Solution()

# Example input
tickets = [2, 3, 2]
k = 2

# Run the function and print the result
print(sol.timeRequiredToBuy(tickets, k))  # Expected output: 6