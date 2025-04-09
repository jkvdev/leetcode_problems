
from typing import List
from collections import Counter
import heapq

# Time: O(n log k)
# Space: O(k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in the input list using Counter
        # This creates a dictionary-like object where keys are the numbers and values are their frequencies
        count = Counter(nums)  # Example: Counter({1: 3, 2: 2, 3: 1})

        # Step 2: Create an empty min-heap (priority queue)
        # We'll store pairs in the form (frequency, number)
        heap = []

        # Step 3: Iterate through the frequency dictionary
        for num, freq in count.items():
            if len(heap) < k:
                # If the heap has less than k elements, just push the (frequency, number) pair
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                # If the current frequency is greater than the smallest in the heap,
                # replace the smallest to maintain the top k most frequent elements
                heapq.heapreplace(heap, (freq, num))

        # Step 4: Extract just the numbers from the (frequency, number) pairs in the heap
        # These are the top k most frequent numbers
        top_k = [num for freq, num in heap]

        return top_k  # Return the result
    
    
# Sample input
nums = [1, 1, 1, 2, 2, 3]
k = 2

# Create an instance and call the method
sol = Solution()
result = sol.topKFrequent(nums, k)

# Print the result
print(result)