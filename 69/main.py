# leetCode: 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
      # Set the search range: left (l) = 1, right (r) = x
      l, r = 1, x
      
      # Binary search
      # Continue searching while left pointer is <= right pointer
      while l <= r:
        # Find the middle element
        m = (l + r) // 2
        
        # If m squared equals x, we found the square root
        if m * m == x:
          return m
        # If m squared is smaller, move 'l' to the right (increase)
        elif m * m < x:
          l = m + 1
        # If m squared is larger, move 'r' to the left (decrease)
        else:
          r = m - 1
          
      # When loop exits, return r (the largest integer whose square is ≤ x)
      return r
    
# Create an instance of Solution
sol = Solution()

# Test with some values
print(sol.mySqrt(4))   # Output: 2
print(sol.mySqrt(8))   # Output: 2 (since sqrt(8) ≈ 2.82, but we return only the integer part)
print(sol.mySqrt(16))  # Output: 4
print(sol.mySqrt(25))
print(sol.mySqrt(36))