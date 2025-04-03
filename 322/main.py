from typing import List

# Coin Change
# Dynamic Programming
# Time: O(n*c)
# Space: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      # number of coins
      n = len(coins) 
      # sort for faster break
      coins.sort() 
      # Dynamic Programming array to store the minimum number of coins needed to make up the amount
      dp = [float('inf')] * (amount + 1)
      # save the number of 0 coins 
      dp[0] = 0 
      
      # iterate through the amount
      for i in range(1, amount + 1):
        # iterate through the coins
        for coin in coins:
          # if the coin is greater than the amount, break
          diff = i - coin
          if diff < 0:
            break
          # update the minimum number of coins needed
          dp[i] = min(dp[i], dp[diff] + 1)
          
      # return the minimum number of coins needed to make up the amount
      return dp[amount] if dp[amount] < float('inf') else -1
    
# To run the function:

solution = Solution()
coins = [1, 2, 5]  # Example coin denominations
amount = 11  # Example amount
result = solution.coinChange(coins, amount)
print(result)  # Output the result