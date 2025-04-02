
from typing import List

# Time: O(n)
# Space O(1)
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)  # Get the length of the array
        longest = 0  # Variable to track the longest mountain found
        i = 1  # Start from the second element since the first element can't be a peak

        while i < n - 1:  # Iterate through the array, stopping at the second-last element
            # Step 1: Check if the current element is a peak (greater than both neighbors)
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l, r = i, i  # Set left (`l`) and right (`r`) pointers at the peak position

                # Step 2: Expand to the left while elements are strictly increasing
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1  # Move left pointer to extend the uphill segment

                # Step 3: Expand to the right while elements are strictly decreasing
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1  # Move right pointer to extend the downhill segment

                # Step 4: Calculate mountain length and update longest if necessary
                longest = max(longest, r - l + 1)

                # Step 5: Move `i` directly to `r` to skip rechecking elements in the mountain
                i = r
            else:
                i += 1  # If no peak is found, simply move to the next element

        return longest  # Return the length of the longest mountain found
    
    
# Example Usage:
arr = [2, 1, 4, 7, 3, 2, 5]
solution = Solution()
result = solution.longestMountain(arr)
print(result)  # Output: 5 (The mountain is [1, 4, 7, 3, 2])