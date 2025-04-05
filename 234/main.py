from typing import Optional

# Time: O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Use the slow and fast pointer approach to find the middle of the list
        slow = fast = head 
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps at a time
            slow = slow.next       # Move slow pointer one step at a time
        # When the loop ends, 'slow' will be at the middle of the list

        # Step 2: Reverse the second half of the linked list starting from 'slow'
        prev = None
        while slow is not None:
            next_pointer = slow.next   # Temporarily store the next node
            slow.next = prev           # Reverse the link
            prev = slow                # Move prev to the current node
            slow = next_pointer        # Move to the next node in the original list
        # At the end of this loop, 'prev' will point to the head of the reversed second half

        # Step 3: Compare the first half and the reversed second half
        left = head      # Start from the beginning of the original list
        right = prev     # Start from the beginning of the reversed second half

        while right is not None:
            if left.val is not right.val:
                return False          # If values don't match, it's not a palindrome
            left = left.next          # Move to the next node in the first half
            right = right.next        # Move to the next node in the reversed second half

        return True  # If all nodes matched, the list is a palindrome

# Helper function to create linked list from list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example test
values = [1, 2, 2, 1]
head = create_linked_list(values)
sol = Solution()
print("Is Palindrome:", sol.isPalindrome(head))  # Output: True
