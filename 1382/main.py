
from typing import Optional
from collections import deque

# Time: O(n)
# Space O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Convert the BST to a sorted array using in-order traversal
        nodes = []               # This list will hold the node values in sorted order
        stack = []               # Stack used for iterative in-order traversal
        current = root           # Start from the root node

        while current or stack:
            while current:
                stack.append(current)  # Push all left nodes onto the stack
                current = current.left
            current = stack.pop()      # Pop the top node
            nodes.append(current.val)  # Add the node value to the sorted list
            current = current.right    # Move to the right subtree

        # Step 2: Convert the sorted array into a balanced BST
        if not nodes:
            return None  # Edge case: empty tree

        mid = len(nodes) // 2
        root = TreeNode(nodes[mid])  # Start building the tree from the middle element

        # Use a queue to build the rest of the tree iteratively
        q = deque()
        # Append left and right sub-ranges to the queue for processing
        q.append((root, 0, mid - 1))              # Left side of the root
        q.append((root, mid + 1, len(nodes) - 1)) # Right side of the root

        while q:
            parent, left, right = q.popleft()     # Take one subrange at a time

            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nodes[mid])      # Create a new node from the middle of the sub-range

                # Attach the new node to the parent as left or right child
                if nodes[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child

                # Enqueue sub-ranges for left and right children of the current node
                q.append((child, left, mid - 1))   # Left subtree
                q.append((child, mid + 1, right))  # Right subtree

        return root  # Return the new balanced root node
    
    
    
# Create an unbalanced BST (e.g., a linked list shaped tree)
# Unbalanced tree: 1 -> 2 -> 3 -> 4
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

# Balance the BST
sol = Solution()
balanced_root = sol.balanceBST(root)

# Print tree in level order to check the structure
def print_level_order(root):
    if not root:
        print("Tree is empty")
        return
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        print("Level:", level)

print_level_order(balanced_root)