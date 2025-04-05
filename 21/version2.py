from typing import Optional

# Time: O(n + m)
# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that serves as the starting point of the merged list.
        # Both 'dummy' and 'curr' point to the same ListNode object initially.
        curr = dummy = ListNode() 

        # Traverse both lists until one of them runs out of nodes
        while list1 and list2: 
            # If the value in list1 is smaller, link it to the merged list
            if list1.val < list2.val: 
                curr.next = list1       # Point current node's next to list1's current node
                list1, curr = list1.next, list1  # Advance list1 and move curr to the newly added node
            else: 
                curr.next = list2       # Point current node's next to list2's current node
                list2, curr = list2.next, list2  # Advance list2 and curr

        # If any nodes are left in either list, append them to the merged list
        if list1 or list2: 
            curr.next = list1 if list1 else list2  # Attach remaining nodes

        # Return the head of the merged list (which starts after the dummy node)
        return dummy.next


def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create the lists
list1 = build_list([1, 3, 5])
list2 = build_list([2, 4, 6])

# Merge the lists
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

# Print result
print_list(merged)
