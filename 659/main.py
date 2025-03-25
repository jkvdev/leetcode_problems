from collections import defaultdict
from typing import List
import heapq

# Time: O(N log M)
# Space: O(N)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Dictionary where keys are numbers and values are min-heaps (priority queues)
        # Each heap stores the lengths of subsequences ending at the key number
        end = defaultdict(list)

        # Iterate through each number in the list
        for num in nums:
            # If there are no subsequences ending at num-1, start a new subsequence
            if num-1 not in end:
                heapq.heappush(end[num], 1) # Start a new subsequence of length 1
            else:
                # Extend the shortest subsequence that ends at num-1
                pre_length = heapq.heappop(end[num-1]) # Get the shortest subsequence

                # If there are no remaining subsequences ending at num-1, remove the key
                if len(end[num-1]) == 0:
                    del end[num-1]

                # Add the extended subsequence (now ending at num) with increased length
                heapq.heappush(end[num], pre_length + 1)

        # After processing all numbers, check if any subsequence has a length < 3
        # If so, return False, as all subsequences must be at least 3 in length
        if any(min(end[num]) < 3 for num in end):
            return False

        return True

# Example usage:
solution = Solution()
nums = [1, 2, 3, 3, 4, 5]
print(solution.isPossible(nums))  # Output: True