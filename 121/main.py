from typing import List  # Import List for type hinting

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Set initial min price to infinity
        max_profit = 0  # Start with zero profit
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min price if a lower price is found
                
            profit = price - min_price  # Calculate current profit
            
            if profit > max_profit:
                max_profit = profit  # Update max profit if a higher profit is found
                
        return max_profit  # Return the maximum profit

# Example test cases
prices = [7, 1, 5, 3, 6, 4]  # Stock prices on different days
sol = Solution()  # Create an instance of the Solution class
print(sol.maxProfit(prices))  # Expected output: 5 (Buy at 1, Sell at 6)

prices2 = [7, 6, 4, 3, 1]  # Prices are in decreasing order
print(sol.maxProfit(prices2))  # Expected output: 0 (No profit possible)
