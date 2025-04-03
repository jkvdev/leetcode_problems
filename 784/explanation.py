from typing import List

# Time Complexity: O(2^n) - Each character can create 2 new strings, leading to exponential growth.
# Space Complexity: O(2^n) - Storing all possible permutations.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = ['']  # Initialize output list with an empty string to build permutations.

        for c in s:  # Iterate over each character in the input string
            print("C", c)  # Print current character being processed
            tmp = []  # Temporary list to store new permutations
            
            if c.isalpha():  # If the character is a letter (not a digit)
                for o in output:  # Iterate over existing permutations
                    print("----------------")
                    print("o in output", o, output)
                    tmp.append(o + c.lower())  # Append lowercase version
                    tmp.append(o + c.upper())  # Append uppercase version
                    print('tmp', tmp)  # Print the intermediate list
                    print("----------------")
            else:  # If the character is a digit
                print("----------------")
                for o in output:
                    print("o in output ", o, output)
                    tmp.append(o + c)  # Simply append the digit (no case change)
                print('tmp after adding num:', tmp)
                print("----------------")

            output = tmp  # Update the output list with the new permutations
            print("Output after main iteration: ", output)

        return output  # Return all possible letter case permutations


# Example usage
sol = Solution()
sol.letterCasePermutation('a1b2')  