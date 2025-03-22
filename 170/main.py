# Linkedin Question

# Premium Leetcode Question
# 170. Two Sum III - Data structure design

# Create a TwoSum class
class TwoSum:
  
    # Create a constructor
    def __init__(self):
      # Create a hashmap
        self.hashmap = {}
        # Create an empty array
        self.arr = []
        # Create a variable to store the number of values stored
        self.n = 0
        
    # Add/store a number in the hashmap
    def add(self, number: int) -> None:
        # Store the key as the number in the hashmap and the value as index
        self.hashmap[number] = self.n
        # Add the number to the array
        self.arr.append(number)
        # Increment the number of values stored
        self.n += 1
        
    # Find if there exists any pair of numbers which sum is equal to the value
    def find(self, value: int) -> bool:
        # Iterate through each number in the array
        for i in range(self.n):
            # Calculate the complement
            complement = value - self.arr[i]
            # If the complement is in the hashmap and the index is not the same as the current index
            if complement in self.hashmap and self.hashmap[complement] != i:
                return True
        return False
      
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