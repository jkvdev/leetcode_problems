
from typing import List

# Apple interview question
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Sum all the apples
        total_apples = sum(apple)
        # Sort in descending order
        capacity.sort(key=lambda x: -x)
        
        # Initialize the number of boxes
        num_boxes = 0
        
        # For each existing box size in the capacity list
        for box_size in capacity:
            # Subtract the box size from the total apples
            total_apples -= box_size
            # Increment the number of boxes
            num_boxes += 1
            
            # If the total apples is less than or equal to 0, return the number of boxes
            if total_apples <= 0: 
                return num_boxes
            
# Define the input lists
apple = [3, 2, 5]   # Number of apples in each group
capacity = [6, 3, 8]  # Capacity of each available box

# Create an instance of the Solution class
sol = Solution()

# Call the function and print the result
print(sol.minimumBoxes(apple, capacity))