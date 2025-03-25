
from collections import Counter

# Time: O(n)
# Space: O(n)
class Solution:
    def isPossible(self, nums):
        count = Counter(nums)  # Count occurrences of each number
        end = Counter()  # Tracks valid subsequences ending at a certain number

        for num in nums:
            if count[num] == 0:
                continue  # Number already used in a subsequence

            # Try to extend an existing subsequence
            if end[num - 1] > 0:  
                end[num - 1] -= 1  # Remove from existing subsequence
                end[num] += 1  # Extend subsequence to end at num
            
            # Start a new subsequence if possible
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1  # Use next number
                count[num + 2] -= 1  # Use the one after that
                end[num + 2] += 1  # Create a new subsequence ending at num + 2

            else:
                return False  # If neither extending nor starting a new one is possible, return False

            count[num] -= 1  # Mark current number as used

        return True


# Example usage:
solution = Solution()
nums = [1, 2, 3, 3, 4, 5]
print(solution.isPossible(nums))  # Output: True