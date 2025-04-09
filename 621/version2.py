
import heapq
from typing import List
from collections import Counter, deque

# Time: O(n log n)
# Space: O(n)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)  # O(n)

        # Create a max-heap using negative frequencies
        maxheap = [-freq for freq in count.values()]
        heapq.heapify(maxheap)  # O(n)

        time = 0  # Track total time units
        q = deque()  # Cooldown queue: stores (remaining_count, time_available)

        # Process tasks until both heap and cooldown queue are empty
        while maxheap or q:
            time += 1  # Each loop iteration = 1 time unit

            if maxheap:
                # Pop most frequent task and reduce its count
                task = 1 + heapq.heappop(maxheap)  # Add 1 because we're using negative numbers
                if task:  # If task still has remaining instances
                    q.append((task, time + n))  # Set cooldown period

            # Re-add task to heap if its cooldown has expired
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time  # Total time to finish all tasks
    
    
# Example usage
sol = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(sol.leastInterval(tasks, n))  # Output: 8