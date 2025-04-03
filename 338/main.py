
from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize an array 'dp' of size (n+1) with all elements set to 0
        # dp[i] will store the number of 1s in the binary representation of 'i'
        dp = [0] * (n + 1)
        # 'offset' keeps track of the most recent power of 2
        offset = 1  
        
        # Loop through numbers from 1 to n
        for i in range(1, n + 1):
            # If 'i' is a power of 2, update 'offset' to the new power of 2
            if offset * 2 == i:
                offset = i  # Update offset to the new power of 2
                
            # Compute number of 1s in binary representation of 'i'
            # Formula: dp[i] = 1 + dp[i - offset]
            # Explanation: 
            #   - 'offset' is the largest power of 2 ≤ i
            #   - Subtracting 'offset' from 'i' removes the most significant 1-bit
            #   - We add 1 because the removed bit was 1
            dp[i] = 1 + dp[i - offset]
        
        # Return the list containing the count of 1s for each number from 0 to n
        return dp
        
        
# Example usage:
sol = Solution()  # Create an instance of the Solution class
n = 5
print(sol.countBits(n))  # Output: [0, 1, 1, 2, 1, 2]