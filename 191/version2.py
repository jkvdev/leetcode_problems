# Time: O(32) / O(1)
# Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter to store the number of 1s in the binary representation
        res = 0  
        
        # Loop while 'n' is not zero
        while n:
            # Check the last bit of 'n' (n % 2 is 1 if the last bit is 1)
            res += n % 2  
            
            # Right shift 'n' by 1 bit (equivalent to integer division by 2)
            # This removes the last bit we just checked
            n = n >> 1  
        
        # Return the total count of 1s in the binary representation
        return res  
        
# Example usage:
sol = Solution()  # Create an instance of the Solution class
num = 11  # Binary: 1011 (3 ones)
print(sol.hammingWeight(num))  # Output: 3

num = 128  # Binary: 10000000 (1 one)
print(sol.hammingWeight(num))  # Output: 1