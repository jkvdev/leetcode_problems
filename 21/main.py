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
        # Create a dummy node to act as the starting point of the merged list
        # `curr` is a pointer we’ll use to build the new list
        curr = dummy = ListNode()

        # Traverse both input lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                # If list1’s value is smaller, add it to the merged list
                curr.next = list1
                list1 = list1.next  # Move forward in list1
            else:
                # If list2’s value is smaller or equal, add it to the merged list
                curr.next = list2
                list2 = list2.next  # Move forward in list2

            curr = curr.next  # Move the pointer in the merged list

        # If any elements remain in list1 or list2, attach them directly
        curr.next = list1 if list1 else list2

        # Return the merged list, skipping the dummy head
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
