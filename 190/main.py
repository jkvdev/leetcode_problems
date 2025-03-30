
# Time: O(1)
# Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize result to store the reversed bits
        
        # Loop through all 32 bits of the integer
        for i in range(32):
            bit = (n >> i) & 1  # Extract the i-th bit from the right (LSB to MSB)
            res = res | (bit << (31 - i))  # Shift the bit to its correct reversed position and set it in res
        
        return res  # Return the reversed binary representation as an integer
    

# Example usage:
sol = Solution()
n = 0b00000010100101000001111010011100  # Example 32-bit number
result = sol.reverseBits(n)
print(bin(result)[2:])  # Print binary representation of reversed number
print(result)  # Print decimal representation