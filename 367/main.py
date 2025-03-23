
# Binary search
# Time: O(log n), Space: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      l, r = 1, num # Initialize left and right pointers
      
      while l <= r: # Binary search loop
        mid = (l + r) // 2 # Find the middle element
        square = mid * mid # Calculate the square of the middle element
        
        if square == num: # If we find a perfect square
          return True
        elif square < num: # If the square is smaller than num, move the left pointer
          l = mid + 1
        else: # If the square is larger than num, move the right pointer
          r = mid - 1
      
      return False # If no perfect square is found
    
    
# Example usage:
solution = Solution()
num = 16  # Test with a perfect square
result = solution.isPerfectSquare(num)
print(f"Is {num} a perfect square? {result}")  # Should print True

num = 14  # Test with a non-perfect square
result = solution.isPerfectSquare(num)
print(f"Is {num} a perfect square? {result}")  # Should print False