from typing import Optional

# Time: O(n)
# Space: O(1)

# Step 1: Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Step 2: Solution class with middleNode method
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 3: Move fast by 2 and slow by 1 until fast reaches the end
        
        # Initialize two pointers, both starting at the head of the linked list.
        # 'slow' will move one step at a time, 'fast' will move two steps at a time.
        slow = fast = head

        # Traverse the list while 'fast' and 'fast.next' are not None.
        # 'fast' moves twice as fast as 'slow'.
        # When 'fast' reaches the end, 'slow' will be at the middle.
        while fast and fast.next:
            slow = slow.next             # Move slow pointer one step forward
            fast = fast.next.next        # Move fast pointer two steps forward

        # When the loop ends, 'slow' will be pointing to the middle node.
        return slow

# Helper function to create a linked list from a list and return the head
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper function to print linked list from a given node
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Step 4: Create the linked list and run the code
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

sol = Solution()
middle = sol.middleNode(head)

# Step 5: Print the result
print("Middle node and onward:")
print_linked_list(middle)
