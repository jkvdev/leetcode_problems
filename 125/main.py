
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: 
        # l (left) starts at the beginning, r (right) starts at the end
        l, r = 0, len(s) - 1  

        # Loop until the two pointers meet
        while l < r:
            # Move the left pointer forward if it's not an alphanumeric character
            if not s[l].isalnum():
                l += 1
                continue  # Skip to the next iteration
            
            # Move the right pointer backward if it's not an alphanumeric character
            if not s[r].isalnum():
                r -= 1
                continue  # Skip to the next iteration

            # Convert both characters to lowercase and compare them
            if s[l].lower() != s[r].lower():
                return False  # If they are different, it's not a palindrome

            # Move both pointers toward the center
            l, r = l + 1, r - 1
        
        # If the entire string was checked without mismatches, it's a palindrome
        return True
  
  
sol = Solution()

# Example test cases
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(sol.isPalindrome("race a car"))  # Expected: False
print(sol.isPalindrome(" "))  # Expected: True
print(sol.isPalindrome("madam"))  # Expected: True
