
from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)  # Convert the list into a set to allow O(1) lookup times
        ret = []  # This list will store the missing numbers
        
        # Iterate through numbers from 1 to n (where n is the length of nums)
        for i in range(1, len(nums) + 1):  
            if i not in set_nums:  # If a number from 1 to n is missing in the set
                ret.append(i)  # Add the missing number to the result list
              
        return ret  # Return the list of missing numbers
      
      
# Example input list
nums = [4,3,2,7,8,2,3,1]

# Create an instance of Solution
solution = Solution()

# Call the function and print the result
print(solution.findDisappearedNumbers(nums))
