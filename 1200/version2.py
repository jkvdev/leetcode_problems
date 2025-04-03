
from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Define an offset to handle negative numbers
        OFFSET = 10**6  # Since numbers are within [-10⁶, 10⁶]
        
        # Step 2: Create a counting array to track the presence of numbers
        # The size is 2 * OFFSET + 1 to cover the entire range from -10⁶ to 10⁶
        count = [0] * (2 * OFFSET + 1)
        
        # Step 3: Populate the counting array
        # Marking presence of each number by setting count[num + OFFSET] = 1
        for num in arr:
            count[num + OFFSET] = 1
        
        # Step 4: Extract the sorted elements from the count array
        sorted_arr = []
        for i in range(2 * OFFSET + 1):  # Iterate over the full range
            if count[i]:  # If the number exists in the original array
                sorted_arr.append(i - OFFSET)  # Convert back to original value
        
        # Step 5: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(sorted_arr)):  # Compare adjacent elements
            min_diff = min(min_diff, sorted_arr[i] - sorted_arr[i - 1])
        
        # Step 6: Collect all pairs with the minimum absolute difference
        res = []
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] == min_diff:
                res.append([sorted_arr[i - 1], sorted_arr[i]])
        
        # Step 7: Return the list of pairs with the minimum difference
        return res
    
    
# Example usage:
solution = Solution()
arr = [4, 2, 1, 3]
output = solution.minimumAbsDifference(arr)
print(output)  # Expected Output: [[1, 2], [2, 3], [3, 4]]