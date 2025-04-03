from typing import List

# Time Complexity: O(2^n) - Each letter in the input string can be either lowercase or uppercase,
# leading to exponential growth in the number of permutations.
# Space Complexity: O(n + 2^n) - Since we store all permutations in `res`, the space usage grows exponentially.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []  # This list will store all possible letter case permutations

        # Helper function to generate permutations using backtracking
        def backtrack(sub='', i=0):
            # print("sub", sub, "i", i)  # Uncomment this line to see the recursion steps
            # Base case: If sub has the same length as s, store it in res
            if len(sub) == len(s):
                res.append(sub)  # Add the completed string to results
                return
            
            # If the current character is a letter, we branch into both lowercase and uppercase
            if s[i].isalpha():
                backtrack(sub + s[i].swapcase(), i + 1)  # Swap case and recurse
            # Process the character as is (digits remain unchanged)
            backtrack(sub + s[i], i + 1)

        backtrack()  # Start recursion
        return res  # Return all possible permutations


# Example usage
sol = Solution()
print(sol.letterCasePermutation('a1b2'))  
