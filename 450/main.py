
from typing import Optional

# Time: O(n)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the tree is empty, just return None
        if not root:
            return None

        parent = None  # This will track the parent of the node we're going to delete
        curr = root    # Start from the root

        # Search for the node with the value equal to 'key'
        while curr and curr.val != key:
            parent = curr  # Update parent before going deeper
            if key < curr.val:
                curr = curr.left  # Move left if key is smaller
            else:
                curr = curr.right  # Move right if key is larger

        # If the key is not found in the tree, return the unchanged root
        if not curr:
            return root

        # Case 1: Node is a leaf (has no children)
        if not curr.left and not curr.right:
            # If it's the root being deleted
            if not parent:
                return None
            # Otherwise, remove the child reference from parent
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node has only one child
        elif not curr.left or not curr.right:
            # Determine which child exists
            child = curr.left if curr.left else curr.right
            # If root is being deleted, return its only child as new root
            if not parent:
                return child
            # Otherwise, connect the parent to the node's only child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node has two children
        else:
            # Find in-order successor (smallest value in right subtree)
            successor_parent = curr
            successor = curr.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Copy the in-order successor's value into current node
            curr.val = successor.val

            # Remove the successor node now (it has at most one child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # Return the (possibly updated) root of the tree
        return root
    
    
    
# Helper function to insert a node into the BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Helper function to print BST in-order (for verification)
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# --- Example usage ---
vals = [5, 3, 6, 2, 4, 7]  # Initial BST
root = None
for v in vals:
    root = insert(root, v)

print("Original tree:", inorder(root))

key_to_delete = 3
solution = Solution()
root = solution.deleteNode(root, key_to_delete)

print("After deletion:", inorder(root))