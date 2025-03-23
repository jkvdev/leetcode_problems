from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
        return None # If the node is None, return None (base case)
      
      # Swap the left and right subtrees
      root.left, root.right = root.right, root.left
      
      # Recursively invert the left and right subtrees
      self.invertTree(root.left)
      self.invertTree(root.right)
      
      return root # Return the root of the inverted tree
    
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