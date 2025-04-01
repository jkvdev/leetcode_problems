
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Create a count array of size 102 (to handle numbers 0-100 safely)
        count = [0] * 102 
        
        # Step 2: Count occurrences of each number
        # We increment count[num + 1] instead of count[num] to simplify prefix sum calculations
        for num in nums:
            count[num + 1] += 1
        
        # Step 3: Compute the prefix sum so that count[i] stores
        # how many numbers are smaller than 'i'
        for i in range(1, 102):
            count[i] += count[i - 1]
        
        # Step 4: Build the result array using the precomputed counts
        # count[num] now tells how many numbers are smaller than 'num'
        return [count[num] for num in nums]
    
# Example run
solution = Solution()
nums = [8, 1, 2, 2, 3]
print(solution.smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]