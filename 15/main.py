
from typing import List

# Time: O(n**2)
# Space: O(1) / O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store the final list of triplets
        nums.sort()  # Sorting the array helps in avoiding duplicates and using two pointers efficiently - O(n log n)
        
        for i, a in enumerate(nums):
            # Skip duplicate elements to prevent duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1  # Initialize two pointers, one at the left and one at the right
            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of the three numbers
                
                if threeSum > 0:  
                    # If the sum is too large, move the right pointer leftward to reduce the sum
                    r -= 1  
                elif threeSum < 0:  
                    # If the sum is too small, move the left pointer rightward to increase the sum
                    l += 1  
                else:  
                    # If the sum is exactly 0, we found a valid triplet
                    res.append([a, nums[l], nums[r]])  
                    
                    # Move the left pointer rightward to find new pairs
                    l += 1
                    
                    # Skip duplicate numbers to avoid duplicate triplets in the result
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  
        
        return res  # Return the final list of triplets
    
    
# Create an instance of the Solution class
sol = Solution()

# Test case
nums = [-1, 0, 1, 2, -1, -4]
result = sol.threeSum(nums)

# Print the output
print(result)  # Expected output: [[-1, -1, 2], [-1, 0, 1]]