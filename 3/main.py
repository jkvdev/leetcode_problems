

# Title: Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dictionary to store the index of the last occurrence of each character
        char_dict = {}
        start = 0
        max_len = 0
        
        # loop through the string
        for end in range(len(s)):
            # if the character is already in the dictionary, update the start index
            if s[end] in char_dict:
                start = max(start, char_dict[s[end]] + 1)
            # update the last occurrence index
            char_dict[s[end]] = end
            # update the longest substring length
            max_len = max(max_len, end - start + 1)
        
        return max_len  # return the longest substring length 
      
      
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(sol.lengthOfLongestSubstring(""))          # Output: 0
print(sol.lengthOfLongestSubstring("dvdf"))      # Output: 3
