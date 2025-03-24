from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      groups = defaultdict(list) # Dictionary to store anagram groups
      
      for s in strs:
          key = [0] * 26 # Array to store letter frequencies (for 'a' to 'z')
          for c in s:
              key[ord(c) - ord('a')] += 1 # Increment count of character
          key = tuple(key) # Convert to tuple to use as a dictionary key
          groups[key].append(s) # Append word to corresponding anagram group
        
      return list(groups.values()) # Return grouped anagrams
    
# Test the function
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print(result)
