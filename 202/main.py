
# Happy number
# Recursively add up all the digits until they get to one
class Solution:
    def isHappy(self, n: int) -> bool:
      # Store seen numbers in a set
      seen = set()
      # Turn the current number into a string
      curr = str(n)
      
      # If the current number hasn't been seen
      while curr not in seen:
          # Add it to the set
          seen.add(curr)
          # Initialize the sum
          sum = 0
          
          # For each digit
          for digit in curr:
              # Turn the digit into an integer
              digit = int(digit)
              # Sum the digit squared to the sum
              sum += digit ** 2
            
          # If the sum is one, the number is happy
          if sum == 1: return True
          # Else, update the current number
          curr = str(sum)
        
      # Not a happy number 
      return False
    
# Create an instance of the Solution class
sol = Solution()

# Test the function with an example
n = 19  # Example input
result = sol.isHappy(n)

# Print the result
print(f"Is {n} a happy number? {result}")