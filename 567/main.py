
# Time: O(n2)
# Space: O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the lengths of both strings
        n1 = len(s1)
        n2 = len(s2)
        
        # If s1 is longer than s2, it's impossible for 
        # s1's permutation to be a substring of s2
        if n1 > n2:
            return False
        
        # Create frequency arrays (size 26, one for each letter in the alphabet)
        s1_counts = [0] * 26
        s2_counts = [0] * 26 # save this for a sliding window
        
        # Initialize the frequency arrays with the first 'n1' characters
        for i in range(n1):
            # Get Ascii values of the characters
            s1_counts[ord(s1[i]) - ord('a')] += 1 # Count characters in s1
            s2_counts[ord(s2[i]) - ord('a')] += 1 # Count characters in the first window of s2
            
        # If the first window already matches, return True
        if s1_counts == s2_counts:
            return True
          
        # Start sliding the window over s2, character by character
        for i in range(n1, n2):
            # Include the new character in the window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
            # Remove the character that is now out of the window (shift left)
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            
            # If the frequency distributions match, we found a valid permutation
            if s1_counts == s2_counts:
                return True
              
        # If no match was found in any window, return False
        return False
            
        
# Test the function
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))  # Expected output: True