
from typing import Optional

# Time: O(n)
# Space: O(1)

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Define the Solution class with the reverseBetween method
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # --- Part 1: Setup and locating the left position ---
        
        # Create a dummy node to handle edge cases (like reversing from the head)
        dummy_head = ListNode(float('-inf'), head)
        
        # Initialize two pointers: one for the node before the left boundary (left_prev)
        # and another pointing to the current node to start reversing from (current_node)
        left_prev, current_node = dummy_head, head
        
        # Move both pointers to their respective positions:
        # left_prev will end up right before the `left`th node
        for i in range(left - 1):
            left_prev = current_node
            current_node = current_node.next
        
        # --- Part 2: Reverse the sublist from left to right ---
        
        prev = None  # This will eventually be the new head of the reversed sublist
        
        # Reverse the sublist between 'left' and 'right' inclusive
        for i in range(right - left + 1):
            next_pointer = current_node.next  # Save the next node
            current_node.next = prev          # Reverse the link
            prev = current_node               # Move prev forward
            current_node = next_pointer       # Move current_node forward
        
        # --- Part 3: Reconnect the reversed sublist back into the list ---
        
        # Connect the tail of the reversed sublist to the rest of the list
        left_prev.next.next = current_node
        
        # Connect the node before 'left' to the new head of the reversed sublist
        left_prev.next = prev
        
        # Return the head of the new list (might be different if we reversed from head)
        return dummy_head.next

# Helper: Convert list to linked list
def list_to_linkedlist(items):
    dummy = ListNode(0)
    curr = dummy
    for item in items:
        curr.next = ListNode(item)
        curr = curr.next
    return dummy.next

# Helper: Convert linked list to list (for easy viewing)
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Step 3: Run the function
sol = Solution()
head = list_to_linkedlist([1, 2, 3, 4, 5])
new_head = sol.reverseBetween(head, 2, 4)

# Step 4: Print the result
print("Reversed Sublist:", linkedlist_to_list(new_head))
