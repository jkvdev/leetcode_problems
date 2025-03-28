
# Time: O(n)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
      # largest to smallest chars, add them up
      # smaller before larger, subtract the smaller
      
      # Mapping of Roman numerals to integer values
      roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
      res = 0  # Initialize result
      # Iterate through the string
      for i in range(len(s)):
        # If a smaller value precedes a larger one, subtract it
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
          res -= roman[s[i]]
        else:
          res += roman[s[i]]  # Otherwise, add the value
          
      return res
    
    
# Running the function with test cases
sol = Solution()

# Example test cases
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("IV"))       # Output: 4
print(sol.romanToInt("IX"))       # Output: 9
print(sol.romanToInt("LVIII"))    # Output: 58  (50 + 5 + 3)
print(sol.romanToInt("MCMXCIV"))  # Output: 1994 (1000 + 900 + 90 + 4)