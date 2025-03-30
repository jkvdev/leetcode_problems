# Time: O(1)
# Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter for the number of 1s in the binary representation
        res = 0  
        
        # Loop until 'n' becomes zero
        while n:
            # Perform bitwise AND operation: n & (n - 1)
            # This removes the rightmost '1' from 'n'
            # 100001
            # 100000 (AND)
            # ______
            # 100000
            # 011111 (AND)
            # ______
            # 000000
            n &= (n - 1)  
            
            # Increment count for each removed '1'
            res += 1  
        
        # Return the total count of 1s in the binary representation
        return res  
    
# Example usage:
sol = Solution()  # Create an instance of the Solution class
num = 11  # Binary: 1011 (3 ones)
print(sol.hammingWeight(num))  # Output: 3

num = 128  # Binary: 10000000 (1 one)
print(sol.hammingWeight(num))  # Output: 1