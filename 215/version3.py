

import heapq
from typing import List

# Time: O(n log k)
# Space: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Create a min-heap with the first k elements of the array
        # These will serve as our top k largest candidates
        heap = nums[:k] 
        # Convert the list into a valid min-heap in O(k) time
        heapq.heapify(heap)

        # Step 2: Iterate over the remaining elements in the array (nums[k:])
        for num in nums[k:]:
            # Only consider elements larger than the smallest in the heap (heap[0])
            # because we're looking for the kth *largest* element
            if num > heap[0]:
                # Replace the smallest element in the heap with the new number
                # and re-heapify in O((n -k) * 2log k) time
                heapq.heapreplace(heap, num)

        # Step 3: After processing all elements, the root of the min-heap (heap[0])
        # will be the kth largest element
        return heap[0]

    
    
# Example usage
sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2

result = sol.findKthLargest(nums, k)
print(f"The {k}th largest element is:", result)