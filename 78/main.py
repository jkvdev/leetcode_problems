from typing import List  # Import List type hint

# All possible array combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) # Get the length of the input list
        path = [] # Temporary list to store the current subset
        res = [] # List to store all subsets
        
        def backtrack(i): # Recursive function
            if i == n: # Base case: if index reaches the end of nums
                res.append(path.copy()) # Store the current subset in the result
                return
            
            next_number = nums[i] # Get the current number
            
            # Option 1: Exclude the current number (Don't add it to the subset)
            backtrack(i+1)
            
            # Option 2: Include the current number
            path.append(next_number)
            backtrack(i+1)
            
            # Backtrack: Remove the last element before returning
            path.pop()
            
            return res # Return the list of subsets
        
        return backtrack(0) # Start recursion from index 0
    
    
# Create an instance of the Solution class
sol = Solution()

# Test the function with an example input
nums = [1, 2, 3]  # Example input
result = sol.subsets(nums)

# Print the result
print(f"Subsets of {nums}: {result}")