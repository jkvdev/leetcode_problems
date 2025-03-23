from typing import List

# Leetcode Problem 11
# Container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1 # Initialize two pointers
        max_area = 0 # Track the maximum area
        
        while l < r: # Continue until the pointers meet
            h = min(height[l], height[r]) # Take the shorter height
            w = r - l # Calculate width
            area = h*w # Compute the area
            max_area = max(max_area, area) # Update max area if necessary
            
            # Move the pointer pointing to the smaller height
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
          
        return max_area # Return the maximum area found
        
      
# Example usage:
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Sample input
sol = Solution()  # Create an instance of the Solution class
result = sol.maxArea(heights)  # Call the function with the height list
print("Maximum Water Area:", result)  # Print the result