
from typing import List

# Time: O(n * n!)
# Space: O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Helper backtrack function
        def backtrack(start, end):
            # If the current permutation is complete (we reached the end)
            if start == end:
                result.append(nums[:])  # Append a copy of the current permutation
                return

            # Iterate through the array, swapping each element with the start index
            for i in range(start, end):
                # Swap nums[start] with nums[i] to fix the current element
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively generate all permutations with the next index fixed
                backtrack(start + 1, end)
                # Swap back to backtrack and try another number at current position
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []  # Holds all the permutations
        backtrack(0, len(nums))  # Start backtracking from index 0
        return result
    
    
# Example usage:
sol = Solution()
nums = [1, 2, 3]
permutations = sol.permute(nums)
print(f"Permutations of {nums}:")
for p in permutations:
    print(p)