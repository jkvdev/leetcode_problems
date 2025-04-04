from typing import Optional

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize 2 pointers
        slow, fast = head, head
        
        # While the fast pointer hasn't reached the end
        while fast and fast.next:
            # Step once for slow
            slow = slow.next
            # Step twice for fast
            fast = fast.next.next
            # If the pointers meet
            if slow == fast:
                # The linked list has a loop
                return True
            
        # No loop found
        return False

# Function to create a cycle in a linked list
def create_cycle(head: ListNode, pos: int) -> ListNode:
    if pos == -1:
        return head  # No cycle

    cycle_node, tail = None, head
    index = 0

    while tail.next:
        if index == pos:
            cycle_node = tail  # Node where the cycle should start
        tail = tail.next
        index += 1

    tail.next = cycle_node  # Create cycle

    return head

# Creating a linked list: 3 -> 2 -> 0 -> -4 -> (cycle back to node 2)
nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head_with_cycle = create_cycle(nodes[0], pos=1)  # Cycle at index 1

# Creating a linked list without a cycle: 1 -> 2 -> 3 -> None
head_no_cycle = ListNode(1)
head_no_cycle.next = ListNode(2)
head_no_cycle.next.next = ListNode(3)

# Testing
sol = Solution()
print("Cycle detected (should be True):", sol.hasCycle(head_with_cycle))
print("Cycle detected (should be False):", sol.hasCycle(head_no_cycle))