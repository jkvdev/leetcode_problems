
from typing import List

# Time: O(n)
# Space: O(n)

# Reversed Polished notation
# (3, 4, +) => 3 + 4
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      
      for t in tokens: 
        # Get Value
        if t not in "+-/*":
          stack.append(int(t))
          
        # Check operand
        else:
          r, l = stack.pop(), stack.pop()
          if t == "+":
            stack.append(l+r)
          elif t == '-':
            stack.append(l-r)
          elif t == '*':
            stack.append(l*r)
          else:
            stack.append(int(float(l)/r))
      
      # Return last item in the stack
      return stack.pop()
            
            
# Create an instance of Solution
sol = Solution()

# Test the method with an RPN expression
tokens = ["2", "1", "+", "3", "*"]
result = sol.evalRPN(tokens)

print(result)  # Output should be 9, as (2 + 1) * 3 = 9