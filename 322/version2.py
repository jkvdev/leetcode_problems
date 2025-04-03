from typing import List

# Coin Change
# Dynamic Programming
# Time: O(n*c)
# Space: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Step 1: Initialize a dynamic programming (dp) array.
        # dp[i] represents the minimum number of coins required to make the amount i.
        # Initialize dp with a large value (amount + 1) because we want to minimize this value.
        dp = [amount + 1] * (amount + 1)
        # dp[0] = 0 because zero coins are needed to make amount 0.
        dp[0] = 0
        
        # Step 2: Iterate through all amounts from 1 to the given 'amount'.
        for i in range(1, amount + 1):
            # Step 3: For each amount i, check all coin denominations.
            for c in coins:
                # If it's possible to subtract the coin value 'c' from the current amount 'i'
                if (i - c) >= 0:
                    # Step 4: Update dp[i] with the minimum number of coins needed
                    # to make amount 'i' (using the current coin 'c').
                    # We compare the current value of dp[i] with 1 + dp[i - c], which represents
                    # using one more coin (coin 'c') to reach amount 'i' by starting from 
                    # amount 'i - c'.
                    dp[i] = min(dp[i], 1 + dp[i - c])
        # Step 5: After filling the dp array, check if we were able to form the 'amount'.
        # If dp[amount] is still greater than amount + 1, it means we couldn't form the 'amount'.
        # In that case, return -1, else return dp[amount], the minimum number of coins needed.
        return dp[amount] if dp[amount] != amount + 1 else -1
    
# To run the function:

solution = Solution()
coins = [1, 2, 5]  # Example coin denominations
amount = 11  # Example amount
result = solution.coinChange(coins, amount)
print(result)  # Output the result