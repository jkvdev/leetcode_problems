
# Problem: Repeated Character
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # List to store seen letters
        # List to store seen letters
        # No need for hash-set because of the fast lookup
        # At most 26 chars
        seen_letters = []
        
        # Iterate through each character in the string
        for c in s:
            # If the character is in seen_letters, return it
            if c in seen_letters:
                return c
            # Otherwise, add it to seen_letters
            else:
                seen_letters.append(c)
                
                
sol = Solution()  # Create an instance of the Solution class

# Test cases
print(sol.repeatedCharacter("abca"))  # Expected output: 'a'
print(sol.repeatedCharacter("abcdef"))  # Expected output: None (No repeated character)
print(sol.repeatedCharacter("racecar"))  # Expected output: 'r'
print(sol.repeatedCharacter("banana"))  # Expected output: 'a'

