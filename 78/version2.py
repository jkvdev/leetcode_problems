
from typing import List  # Import List type hint

# All possible array combinations
# Time: O(n*2^n)
# Space: O(n*2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:]) # append copy of path snapshot
            
            # print(start, path)
            # print("Result:", result)
            # print("----------------")
            
            for i in range(start, len(nums)):
              path.append(nums[i]) # include nums[i] in the subset
              backtrack(i +1, path) # continue to build subset from the next element
              path.pop() # exclude the nums[i] from the subset (backtrack)
              

            
        result = []
        backtrack(0, [])
        return result
    
    
# Create an instance of the Solution class
sol = Solution()

# Test the function with an example input
nums = [1, 2, 3]  # Example input
result = sol.subsets(nums)

# Print the result
print(f"Subsets of {nums}: {result}")