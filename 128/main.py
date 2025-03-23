from typing import List

# leetCode: 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      numSet = set(nums) # Convert the list to a set for O(1) lookups
      longest = 0 # Store the longest sequence size
      
      # Iterate through the set
      for n in numSet:
        # If n - 1 is not in the set, then n is the start of a sequence
        if n - 1 not in numSet:
          # Start the length of the sequence
          length = 1
          # while n + length is in the set, increment the length
          while n + length in numSet:
            length += 1
          # Update the longest sequence size
          longest = max(longest, length)
          
      # Return the longest sequence size
      return longest
    
# Example usage:
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
result = solution.longestConsecutive(nums)
print(result)  # Output should be 4 because the longest consecutive sequence is [1, 2, 3, 4]