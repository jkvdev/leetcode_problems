
# Time: O(A + B)
# Space: O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)  # Convert binary strings to integers
        
        while b:  # Perform binary addition using bitwise operations
            without_carry = a ^ b  # XOR for sum without carry
            carry = (a & b) << 1   # AND + left shift for carry
            
            a, b = without_carry, carry  # Update a and b for next iteration
        
        return bin(a)[2:]  # Convert result back to binary and remove '0b' prefix

# Example usage:
sol = Solution()
result = sol.addBinary("1010", "1011")
print(result)  # Expected output: "10101"
