

# Title: Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dictionary to store the index of the last occurrence of each character
        last_occurrence = {}
        start = 0
        longest = 0
        
        # loop through the string
        for i, char in enumerate(s):
            # if the character is already in the dictionary, update the start index
            if char in last_occurrence:
                start = max(start, last_occurrence[char] + 1)
            # update the last occurrence index
            last_occurrence[char] = i
            # update the longest substring length
            longest = max(longest, i - start + 1)
        
        return longest  # return the longest substring length 
      
      