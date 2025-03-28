from typing import List  # Import List for type hinting

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: If there are no heights or less than 3 elements, no water can be trapped
        if not height or len(height) < 3:
            return 0
        
        # Initialize left and right boundary walls
        l_wall = r_wall = 0 
        n = len(height)

        # Arrays to store the highest wall seen to the left and right of each position
        max_left = [0] * n  
        max_right = [0] * n  

        # Step 1: Precompute max_left and max_right for each index
        for i in range(n):
            j = -i -1  # Reverse index to traverse from the right simultaneously

            # Store the highest wall to the left (excluding current position)
            max_left[i] = l_wall  
            # Store the highest wall to the right (excluding current position)
            max_right[j] = r_wall  

            # Update the left and right boundary walls as we traverse
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        # Step 2: Calculate trapped water for each position
        ans = [0] * n  # Array to store trapped water at each position

        for i in range(n):
            # The water level at index i is determined by the smaller of the two walls
            potential = min(max_left[i], max_right[i])

            # If the potential water level is higher than the current height, water is trapped
            ans[i] = max(0, potential - height[i])

        # Step 3: Sum up all trapped water values
        return sum(ans)  # Return the total trapped water

# Example test cases
sol = Solution()

# Test case 1
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]  # Expected output: 6
print(sol.trap(height1))

# Test case 2
height2 = [4,2,0,3,2,5]  # Expected output: 9
print(sol.trap(height2))
