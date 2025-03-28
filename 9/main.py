
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If the number is negative, it cannot be a palindrome
        if x < 0:
            return False
        
        # Initialize the 'div' variable to find the highest place value
        div = 1
        # Loop to find the highest power of 10 less than or equal to x
        while x >= 10 * div:
            div *= 10
        
        # While the number 'x' has digits to check
        while x:
            # Get the rightmost digit (last digit)
            right = x % 10
            # Get the leftmost digit by dividing x by 'div'
            left = x // div
            
            # If the left and right digits don't match, it's not a palindrome
            if left != right:
                return False
            
            # Remove the leftmost digit from 'x' by using modulo and integer division
            x = (x % div) // 10
            # Update the 'div' value by reducing it by two places (dividing by 100)
            div = div / 100
        
        # If the loop completes without returning False, it's a palindrome
        return True
    
    
# Create an instance of the Solution class
sol = Solution()

# Test cases
print(sol.isPalindrome(121))  # Output: True (121 is a palindrome)
print(sol.isPalindrome(-121)) # Output: False (Negative numbers are not palindromes)
print(sol.isPalindrome(10))   # Output: False (10 is not a palindrome)
print(sol.isPalindrome(1221)) # Output: True (1221 is a palindrome)
