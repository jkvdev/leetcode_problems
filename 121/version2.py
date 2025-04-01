from typing import List  # Import List for type hinting

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers:
        # l (left) represents the day we buy the stock
        # r (right) represents the day we sell the stock
        l, r = 0, 1
        # Variable to keep track of the maximum profit found
        maxP = 0  
        
        # Iterate through the list using the right pointer
        while r != len(prices):  
            # If the price at left pointer (buy price) is lower than right pointer (sell price)
            if prices[l] < prices[r]:  
                # Calculate profit if we buy at l and sell at r
                prof = prices[r] - prices[l]  
                # Update maxP if this profit is greater than our previous max
                maxP = max(maxP, prof)  
            else:
                # If the current price is lower than our buy price,
                # move the buy pointer to the current day (we only want to buy at the lowest possible price)
                l = r  
            # Move the right pointer forward to check the next day
            r += 1  
        # Return the maximum profit found
        return maxP 
        

# Example test cases
prices = [7, 1, 5, 3, 6, 4]  # Stock prices on different days
sol = Solution()  # Create an instance of the Solution class
print(sol.maxProfit(prices))  # Expected output: 5 (Buy at 1, Sell at 6)

prices2 = [7, 6, 4, 3, 1]  # Prices are in decreasing order
print(sol.maxProfit(prices2))  # Expected output: 0 (No profit possible)
