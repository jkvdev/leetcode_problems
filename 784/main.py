from typing import List

# Time Complexity: O(2^n) 
# Space Complexity: O(2^n) 
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = ['']  # Initialize output list with an empty string to build permutations.

        for c in s:  # Iterate over each character in the input string
            tmp = []  # Temporary list to store new permutations
            
            if c.isalpha():  # If the character is a letter (not a digit)
                for o in output:  # Iterate over existing permutations
                    tmp.append(o + c.lower())  # Append lowercase version
                    tmp.append(o + c.upper())  # Append uppercase version
            else:  # If the character is a digit
                for o in output:
                    tmp.append(o + c)  # Simply append the digit (no case change)

            output = tmp  # Update the output list with the new permutations

        return output  # Return all possible letter case permutations


# Example usage
sol = Solution()
print(sol.letterCasePermutation('a1b2'))