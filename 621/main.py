
import heapq
from typing import List
from collections import Counter, deque

# Time: O(n log n)
# Space: O(n)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count how many times each task appears
        task_counts = Counter(tasks)  # O(n), where n is the number of tasks

        # Step 2: Build a max-heap from the task frequencies
        # We use negative counts because Python's heapq is a min-heap by default
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)  # O(n)

        # Step 3: Set up variables
        time = 0  # Total time taken to complete all tasks
        wait_queue = deque()  # Queue to keep track of tasks in cooldown; stores (task_count, time_available)

        # Step 4: Run the task scheduling loop
        while max_heap or wait_queue:
            time += 1  # Increment time for each CPU cycle

            if max_heap:
                # Pop the most frequent task (negative count, so smallest number)
                curr_task = heapq.heappop(max_heap)
                curr_task += 1  # Decrease count (because it's negative, this brings it closer to 0)

                # If the task still has remaining counts, put it in the cooldown queue
                if curr_task != 0:
                    # Task will be available again after n units of time
                    wait_queue.append((curr_task, time + n))

            # If the task at the front of the cooldown queue is ready, push it back into the heap
            if wait_queue and wait_queue[0][1] == time:
                ready_task = wait_queue.popleft()[0]
                heapq.heappush(max_heap, ready_task)

        # Step 5: Return total time taken to process all tasks with cooldowns
        return time
    
    
# Example usage
sol = Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(sol.leastInterval(tasks, n))  # Output: 8