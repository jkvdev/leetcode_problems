

import heapq
from typing import List

# Time: O(n log n)
# Space: O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # Initialize an empty min-heap (by default, heapq implements a min-heap)

        # Push all elements of the array into the heap
        for i in nums:
            heapq.heappush(heap, i)  # Adds each element to the heap, maintaining the heap property

        # Pop the smallest elements (len(nums) - k) times
        # This leaves the k largest elements in the heap
        for i in range(len(nums) - k):
            heapq.heappop(heap)  # Removes the smallest element each time

        # The next popped element is the kth largest
        return heapq.heappop(heap)
    
    
# Example usage
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2

result = sol.findKthLargest(nums, k)
print(f"The {k}th largest element is:", result)