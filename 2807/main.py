import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Inserts a new node containing the Greatest Common Divisor (GCD)
        between every two adjacent nodes in the linked list.
        """
        curr = head.next # Start from the second node
        prev = head # Keep track of the previous node
        
        while curr: 
            gcd = math.gcd(curr.val, prev.val) # Compute GCD of two adjacent nodes
            gcd_node = ListNode(gcd) # Create a new node with the GCD value
            
            prev.next = gcd_node # Insert GCD node after previous node
            gcd_node.next = curr # Connect the GCD node to the current node
            
            prev = curr # Move to the next node pair
            curr = curr.next # Advance to the next node
          
        return head # Return the modified linked list
      
      
      
# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Function to print a linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

# Example usage:
values = [18, 24, 30]  # Example list
head = create_linked_list(values)

print("Original linked list:")
print_linked_list(head)

sol = Solution()
modified_head = sol.insertGreatestCommonDivisors(head)

print("Modified linked list:")
print_linked_list(modified_head)
