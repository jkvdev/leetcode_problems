from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the current node is None, return None
        if root:
            # Recursively invert the right subtree and assign it to the left child
            # Recursively invert the left subtree and assign it to the right child
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        # Return the current root after its left and right children have been swapped
        return root
        
      # Time: O(n)
      # Space: O(h) where h = height of the tree
      
# Function to print the tree (in-order traversal)
def printTree(root: Optional[TreeNode]):
    if root:
        printTree(root.left)
        print(root.val, end=" ")
        printTree(root.right)

# Example Usage:
# Construct the binary tree:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (In-order):")
printTree(root)  # Before inverting

# Invert the tree
sol = Solution()
root = sol.invertTree(root)

print("\nInverted Tree (In-order):")
printTree(root)  # After inverting