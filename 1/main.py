# Task: Two Sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define dictionary
        num_dict = {}

        # Loop through the number list
        for i, num in enumerate(nums):
            # find the current list number complement
            complement = target - num

            # if the complement exists in the dictionary
            if complement in num_dict:
                # return the complement's and the current number's index
                return [num_dict[complement], i]
            
            # Save the current list number and its index
            num_dict[num] = i

        # Return and empty array if there is no such pair
        return []


# Create an instance of the class
solution = Solution()

# Call the function
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)

# Print the result
print(result)  # Output: [0, 1]