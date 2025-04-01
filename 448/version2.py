
from typing import List

# Time: O(n)
# Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): 
            # Convert the value at index i to an index in the range [0, n-1]
            temp = abs(nums[i]) - 1  
            # If the number at index 'temp' is positive, mark it as visited by making it negative
            if nums[temp] > 0:
                nums[temp] *= -1  

        res = []  # This list will store the missing numbers
        for i, n in enumerate(nums):  
            # If a number is still positive, its index +1 is missing from the original list
            if n > 0:
                res.append(i + 1)  

        return res  # Return the list of missing numbers
            
      
# Example input list
nums = [4,3,2,7,8,2,3,1]

# Create an instance of Solution
solution = Solution()

# Call the function and print the result
print(solution.findDisappearedNumbers(nums))
