
# Source: https://leetcode.com/problems/fibonacci-number/

# Leetcode question 509: Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
# 
# Example 1:
# Input: n = 2
# Output: 1
#
# Example 2:
# Input: n = 3
# Output: 2
class Solution:
    def fib(self, n: int) -> int:
      # Count up from the start
      # Get base cases 
      ans = [0,1]
      
      # Compute Fibonacci numbers iteratively
      for i in range(2,n+1):
          # Append the sum of the previous two values
          ans.append(ans[i-1]+ans[i-2])
      
      # Return the value at the nth index
      return ans[n]
    
# Create an instance of the Solution class
sol = Solution()

# Call the fib method with the desired input
print(sol.fib(10))  # Output: 55
