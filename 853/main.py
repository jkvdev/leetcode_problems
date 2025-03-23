from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      # Pair the positions and speeds of the cars
      pair = [(p, s) for p, s in zip(position, speed)]
      
      stack = [] # To track the fleets
      
      # Sort the pairs by position
      for p, s in sorted(pair):
        # Calculate the time it will take for the car to reach the target
        time = (target - p) / s
        # If the car can catch up to the one ahead of it, pop it from the stack
        while stack and time >= stack[-1]:
          stack.pop()
        # Push the current car's time to the stack
        stack.append(time)
        
      # The number of fleets will be equal to the number of different times in the stack
      return len(stack)
    
# Example usage
solution = Solution()

# Test case 1: cars with different positions and speeds
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

result = solution.carFleet(target, position, speed)
print(f"Number of car fleets: {result}")  # Output should be the number of fleets