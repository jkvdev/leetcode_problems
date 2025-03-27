
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" # store palindrome string
        resLen = 0 # store palindrome length
        
        # go over each character 
        for i in range(len(s)):
            # Check for odd-length palindromes (centered at one character)
            l, r = i, i # Both pointers start at the same index
            
            # Expand around the center while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update the longest palindrome if the current one is longer
                if (r - l + 1) > resLen:
                    res = s[l : r + 1] # Store the palindrome substring
                    resLen = r - l + 1 # Update the longest length
                l -= 1 # Expand to the left
                r += 1 # Expand to the right
        
            # Check for even-length palindromes (centered between two characters)
            l, r = i, i + 1 # Two adjacent characters as the center
            
            # Expand around the center while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update the longest palindrome if the current one is longer
                if (r - l + 1) > resLen:
                    res = s[l : r + 1] # Store the palindrome substring
                    resLen = r - l + 1 # Update the longest length
                l -= 1 # Expand to the left
                r += 1 # Expand to the right
                
        # Return the longest palindromic substring found
        return res
      
      
# Example Usage
solution = Solution()
test_string = "babad"
result = solution.longestPalindrome(test_string)

# Print the result
print(f"Longest Palindromic Substring: {result}")