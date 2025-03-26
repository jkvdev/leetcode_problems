
from typing import List  # Import the List type

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs) # Get the length of the sting
        i = 0 # Initialize counter
        min_length = float('inf') # Initialize minimum length to infinity
        for s in strs:
            if len(s) < min_length:
                min_length = len(s) # Find the length of the shortest string

        # Loop to compare characters in all strings
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i] # If characters do not match, return prefix up to the current index
            i += 1 # Continue to the next character

        return strs[0][:i] # Return the longest common prefix


# Example usage
solution = Solution()
strs = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix(strs)
print(result)  # Output: "fl"