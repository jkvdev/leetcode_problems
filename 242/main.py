from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # Hashmap for counting string letters
      counter_s = Counter(s)
      counter_t = Counter(t)
      
      # Check if they have the same values
      return counter_s == counter_t
      
# Example usage:
sol = Solution()

# Test case 1: Anagram
print(sol.isAnagram("anagram", "nagaram"))  # Should return True

# Test case 2: Not anagram
print(sol.isAnagram("rat", "car"))  # Should return False