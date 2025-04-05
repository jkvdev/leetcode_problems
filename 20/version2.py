
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of open brackets
        stack = [] 
        # Dictionary to map closing brackets to their corresponding opening brackets
        hashmap = {")" : "(", "]" : "[", "}" : "{"} 
        
        # Iterate through each character in the input string.
        for element in s:
            # If there is an open bracket at the top of the stack and the current character  
            # is a closing bracket, check if the top of the stack matches the corresponding 
            # opening bracket.
            if stack and (element in hashmap and 
                          stack[-1] == hashmap[element]):
                # If the brackets match, pop the open bracket from the stack.
                stack.pop()
            else:
                # If the brackets don't match, push the current bracket onto the stack.
                stack.append(element)
        
        # Return True if the stack is empty (all brackets matched), False otherwise.
        return not stack


# Test cases
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True
