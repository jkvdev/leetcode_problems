# No recursion needed
# Time: O(n)
# Space: O(1)

# How many ways could you climb up a certain number of stairs
# Fibonacci sequence approach
class Solution:
    def climbStairs(self, n: int) -> int:
      # Base cases
      if n == 1: return 1
      if n == 2: return 2
      
      # Set default of how many stairs would be climbed by
      # taking 1 or 2 steps at a time
      two_back, one_back = 1, 2
      
      # Go over the other cases than the default ones
      for i in range (2, n):
          # Calculate fibonacci sequence
          curr = two_back + one_back
          # Update the previous steps
          two_back = one_back
          one_back = curr
        
      return curr
    
# Create an instance of the Solution class
sol = Solution()

# Test with an example input
n = 5
result = sol.climbStairs(n)

# Print the output
print(f"Number of ways to climb {n} stairs: {result}")
