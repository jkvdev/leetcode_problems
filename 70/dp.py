# No recursion needed
# Time: O(n)
# Space: O(1)

# How many ways could you climb up a certain number of stairs
# Fibonacci sequence approach
class Solution:
    def climbStairs(self, n: int) -> int:
      # Step 1: Initialize a dp array where dp[i] represents the number 
      # of ways to reach the ith step.
      dp = [0] * (n+1)
      
      # Step 2: Base cases (Initialize the first few steps):
      if n == 1: return 1
      if n == 2: return 2
      
      dp[1], dp[2] = 1, 2
      
      # Step 3: Use dynamic programming to calculate the number of ways for 
      # each step i from 3 to n.
      # The number of ways to reach step i is the sum of the number of ways to 
      # reach the previous step (i-1) 
      # and the step before that (i-2), because you can either take a 1-step or 
      # a 2-step move to get to step i.
      for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
      # Step 4: Return the number of ways to reach the nth step, 
      # which is stored in dp[n].
      return dp[n]
      
    
# Create an instance of the Solution class
sol = Solution()

# Test with an example input
n = 5
result = sol.climbStairs(n)

# Print the output
print(f"Number of ways to climb {n} stairs: {result}")
