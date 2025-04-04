
# Time: O(n)
# Space: O(1)

from typing import Optional

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Define the Solution class with removeElements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy head node with an arbitrary value (not part of the original list)
        # This helps simplify edge cases like removing the actual head node
        dummy_head = ListNode(-1)
        dummy_head.next = head  # Point dummy's next to the real head of the list

        # Initialize a pointer starting at the dummy node
        current_node = dummy_head

        # Traverse the list until the end
        while current_node.next is not None:
            # If the next node's value matches the target value
            if current_node.next.val == val:
                # Remove it by skipping over it (bypass it in the linked list)
                current_node.next = current_node.next.next
            else:
                # Otherwise, move to the next node
                current_node = current_node.next

        # Return the new head of the list (which might have changed), skipping dummy
        return dummy_head.next

# Helper function to create a linked list from a Python list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Step 3: Create a sample linked list and run removeElements
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
val_to_remove = 6

sol = Solution()
new_head = sol.removeElements(head, val_to_remove)

# Step 4: Print the result
print_linked_list(new_head)
