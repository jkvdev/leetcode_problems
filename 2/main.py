# Link: https://leetcode.com/problems/add-two-numbers/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
# Solution class
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # placeholder node for the result
        dummy_head = ListNode(0)
        # current selection / pointer to help build the new linked list
        curr = dummy_head
        # carry for double digit numbers
        carry = 0
        
        # keep looping while the lists exist or there is still a carry value
        while l1 or l2 or carry:
            # Get the current list value and set it to 0 if it doesn't exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # sum the values, divide by 10, save the result into the carry variable 
            # and the remaineder inside of the sum_val variable 
            carry, sum_val = divmod(val1 + val2 + carry, 10)
        
            # get the sum_val and output it into the new linked list
            curr.next = ListNode(sum_val)
            # shift output to next node
            curr = curr.next

            # get the next node if it exists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # restun the new list
        return dummy_head.next
      
      
# Helper function to create a linked list from a list of numbers
def create_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

# Input numbers as linked lists
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

# Call the function
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result
print_linked_list(result)  # Output: 7 -> 0 -> 8 (Represents 807)