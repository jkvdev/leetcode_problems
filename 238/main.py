from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [0] * n, [0] * n  # Initialize left and right product arrays
        l, r = 1, 1  # Variables to store cumulative products

        for i, num in enumerate(nums):
            left[i] = l  # Store cumulative product of left elements
            j = -i -1  # Access from the end of the list
            right[j] = r  # Store cumulative product of right elements
            
            l *= nums[i]  # Update left cumulative product
            r *= nums[j]  # Update right cumulative product
            
        return [l * r for l, r in zip(left, right)]  # Multiply left and right products

# Example usage
solution = Solution()
nums = [1, 2, 3, 4]  
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
