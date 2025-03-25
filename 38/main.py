
class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: when n is 1, return the starting point of the sequence
        if n == 1: return '1'
        # Start with the first term in the sequence
        curr = '1'
        
        # Loop to generate the n-th term
        # We already have the first term ('1'), so we loop n-1 times to generate the next terms
        for i in range(n-1):
            new_str = [] # This will hold the next term in the sequence
            looking = False # Flag to check if we are currently counting a sequence of digits
            count = 0 # To count the occurrences of the current digit
            looking_for = '' # Holds the digit we are currently counting (initialized here)
            
            # Loop through each character in the current term (starting with '1')
            for j in range(len(curr)):
                if looking: # If we're already looking for a digit sequence
                    if curr[j] == looking_for: # If the current digit matches the digit we're counting
                        count += 1 # Increment the count of this digit
                    else: # If the current digit is different from the one we're counting
                        # Append the count and the digit to the new string
                        new_str.append(f'{count}{looking_for}')
                        # Reset to count the new digit
                        looking_for = curr[j]
                        count = 1 # Restart the count for the new digit
                else: # If it's the first time we are encountering a digit sequence
                    count = 1 # Start counting this new digit
                    looking_for = curr[j] # Set the digit we're counting
                    looking = True # Mark that we're counting now
                    
            # After the loop ends, there will be one last sequence to count
            new_str.append(f'{count}{looking_for}')
            # Join the new string (this will be the next term in the sequence)
            curr = ''.join(new_str)
            
        # Return the final term in the sequence
        return curr
        
        
# Create an instance of the Solution class
solution = Solution()

# Call the countAndSay method with the desired value of n
n = 5
result = solution.countAndSay(n)

# Print the result
print(result)  # Expected output: '111221'

