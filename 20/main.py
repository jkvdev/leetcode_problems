
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of open brackets
        stack = [] 
        # Dictionary to map closing brackets to their corresponding opening brackets
        close_to_open = {")" : "(", "]" : "[", "}" : "{"} 
        
        # Iterate through each character in the string
        for c in s:
            # If the character is an opening bracket, push it onto the stack
            if c not in close_to_open:
                stack.append(c)
                continue # Move to the next character

            # If it's a closing bracket, check if the stack is empty 
            # or the top of the stack is not the matching opening bracket
            if not stack or stack[-1] != close_to_open[c]:
                return False # If there's a mismatch, the string is not valid

            # If the top of the stack matches the corresponding 
            # opening bracket, pop it from the stack
            stack.pop()
        
        # If the stack is empty at the end, all brackets were properly closed, return True
        return len(stack) == 0


# Test cases
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True
