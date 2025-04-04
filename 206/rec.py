
from typing import Optional

# Time: O(n)
# Space: O(1)
# Recursive

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Define the Solution class with the reverseList method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one element, return it as is
        if not head or not head.next:
            return head  # Returning the last node or None (end of recursion)
        
        # Recursive case: Call reverseList on the rest of the list
        reversed_head = self.reverseList(head.next)
        
        # Now head.next points to the last node of the original list
        # We want to reverse the links, so we do the following:
        
        # Set the next node's next pointer to the current node (head)
        head.next.next = head  # This step connects the current node (head) to the reversed part
        
        # Set the current node's next pointer to None (since it will be the last node after reversal)
        head.next = None  # The node currently at the head should become the tail, so it points to None
        
        # Return the reversed list's head (which is the new head of the list)
        return reversed_head  # This will propagate the new head back through the recursion

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
