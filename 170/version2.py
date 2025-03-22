# Linkedin Question

# Premium Leetcode Question
# 170. Two Sum III - Data structure design

# Create a TwoSum class
class TwoSum:
  
    # Create a constructor
    def __init__(self):
        # Create a hashmap to store numbers and their frequency
        self.hashmap = {}
        
    # Add/store a number in the hashmap
    def add(self, number: int) -> None:
        # Store the number in the hashmap and increase its frequency
        self.hashmap[number] = self.hashmap.get(number, 0) + 1
        
    # Find if there exists any pair of numbers whose sum is equal to the value
    def find(self, value: int) -> bool:
        # Iterate through each unique number in the hashmap
        for num in self.hashmap:
            # Calculate the complement
            complement = value - num
            # If the complement exists in the hashmap
            if complement in self.hashmap:
                # If the complement is different or appears at least twice, return True
                if complement != num or self.hashmap[num] > 1:
                    return True
        # Return False if no valid pair is found
        return False


# Example Usage:
# Create an instance of the TwoSum class
two_sum = TwoSum()

# Add numbers to the data structure
two_sum.add(1)
two_sum.add(3)
two_sum.add(5)

# Test the find method
print(two_sum.find(4))  # Expected output: True (1 + 3 = 4)
print(two_sum.find(8))  # Expected output: True (3 + 5 = 8)
print(two_sum.find(10)) # Expected output: False (No two numbers sum to 10)
