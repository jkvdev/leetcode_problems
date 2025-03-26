
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)  # get length
        l, r = 0, n-1 # start 2 pointers
        
        # while pointers are not matching
        while l < r:
            sum = numbers[l] + numbers[r] # get sum
            if sum == target:
                return [l+1, r+1] # return 1 based indices
            # if sum is smaller than target
            elif sum < target:
                l += 1 # move inwards form left
            else:
                r -= 1 # move inwards form right
                
                
# Example Usage
solution = Solution()
numbers = [2, 7, 11, 15]
target = 9
result = solution.twoSum(numbers, target)
print(result)  # Output: [1, 2]