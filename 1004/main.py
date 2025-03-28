from typing import List  # Import List for type hinting

# Time: O(n)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Variable to store the maximum length of the sub-array with at most k flips
        max_window = 0  
        # Counter to keep track of the number of zeros in the current window
        num_zeros = 0  

        # Left pointer of the sliding window
        l = 0  
        # Iterate through the list using the right pointer `r`
        for r in range(len(nums)):
            # If the current element is 0, increase the zero count
            if nums[r] == 0:
                num_zeros += 1

            # If the count of zeros exceeds k, shrink the window from the left
            while num_zeros > k:
                if nums[l] == 0:  # If the leftmost element is 0, reduce zero count
                    num_zeros -= 1
                l += 1  # Move the left pointer forward to maintain k flips

            # Update the maximum window size found so far
            max_window = max(max_window, (r - l + 1))

        # Return the maximum contiguous sub-array length found
        return max_window

# Create an instance of Solution
sol = Solution()

# Example test cases
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,1,1], 3))  # Output: 12
print(sol.longestOnes([1,0,1,1,0,1,1,1,0,0,1,1,1,1], 2))  # Output: 9
