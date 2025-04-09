

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
    # Helper function to find the node with the smallest value in a subtree
    def _find_min_node(self, node: TreeNode) -> TreeNode:
        # In a BST, the leftmost node is the smallest
        while node.left:
            node = node.left
        return node

    # Main function to delete a node with a given key from the BST
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root  # Start from the root node

        # Base case: If the tree is empty, return None
        if not curr:
            return None

        # If the key to be deleted is smaller than the current node's value,
        # recurse into the left subtree
        if key < curr.val:
            curr.left = self.deleteNode(curr.left, key)

        # If the key to be deleted is greater than the current node's value,
        # recurse into the right subtree
        elif key > curr.val:
            curr.right = self.deleteNode(curr.right, key)

        # If the key matches the current node's value, we've found the node to delete
        else:
            # Case 1: Node has no children (leaf node)
            if not curr.left and not curr.right:
                return None  # Just remove it by returning None

            # Case 2a: Node has only a right child
            elif not curr.left:
                return curr.right  # Replace node with its right child

            # Case 2b: Node has only a left child
            elif not curr.right:
                return curr.left  # Replace node with its left child

            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest value in right subtree)
                temp = self._find_min_node(curr.right)

                # Replace current node's value with the successor's value
                curr.val = temp.val

                # Recursively delete the in-order successor (to avoid duplicate)
                curr.right = self.deleteNode(curr.right, temp.val)

        # Return the current (possibly updated) node to link back to its parent
        return curr
    
    
    
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