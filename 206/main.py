
from typing import Optional

# Time: O(n)
# Space: O(1)
# Iterative

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Define the Solution class with the reverseList method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_pointer = curr.next  # Store next node
            curr.next = prev          # Reverse the current node's pointer
            prev = curr               # Move prev to current node
            curr = next_pointer       # Move to the next node

        return prev  # New head of the reversed list

# Step 3: Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Step 4: Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1

# Step 5: Reverse and print the linked list
sol = Solution()
reversed_head = sol.reverseList(head)
print("Reversed Linked List:")
print_linked_list(reversed_head)
