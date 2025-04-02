
from typing import List

# Time: O(n)
# Space O(1)
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ret = 0  # Variable to store the maximum mountain length
        
        # Iterate through the array, starting from the second element (index 1) to the second-last element
        for i in range(1, len(arr) - 1):
            # Check if the current element forms a peak (i.e., greater than both its neighbors)
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l, r = i, i  # Initialize left and right pointers at the peak
                
                # Expand the left boundary of the mountain while the sequence is increasing
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1  # Move left
                
                # Expand the right boundary of the mountain while the sequence is decreasing
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1  # Move right
                
                # Calculate the mountain length and update the maximum length found
                ret = max(ret, r - l + 1)
        
        return ret  # Return the maximum mountain length found
    
    
# Example Usage:
arr = [2, 1, 4, 7, 3, 2, 5]
solution = Solution()
result = solution.longestMountain(arr)
print(result)  # Output: 5 (The mountain is [1, 4, 7, 3, 2])