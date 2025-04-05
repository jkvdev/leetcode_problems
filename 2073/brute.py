
from typing import List

# Time: O(n*m)
# Space: O(n)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0  # Tracks the total time (seconds) taken
        
        # Keep looping until the person at index 'k' has no tickets left
        while True:
            # Iterate over each person in the queue
            for i in range(len(tickets)):
                
                # If the person at position 'k' has finished buying all tickets, return the total time
                if tickets[k] == 0:
                    return time
                
                # Skip if the current person has already bought all their tickets
                if tickets[i] == 0:
                    continue
                
                # Otherwise, the current person buys one ticket
                tickets[i] -= 1  # Reduce their remaining tickets by 1
                time += 1        # Increment the total time (1 second per ticket purchase)
    
    
# Create an instance of Solution
sol = Solution()

# Example input
tickets = [2, 3, 2]
k = 2

# Run the function and print the result
print(sol.timeRequiredToBuy(tickets, k))  # Expected output: 6