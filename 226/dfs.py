from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Initialize a stack for iterative DFS traversal. Start with the root node.
        stack = [root]

        # Continue processing while there are nodes in the stack
        while stack:
            # Pop the last node added to the stack (DFS behavior)
            curr = stack.pop()

            # Only process non-null nodes
            if curr:
                # Swap the left and right children of the current node
                curr.left, curr.right = curr.right, curr.left

                # Add the children to the stack to process them later
                # (after swapping, we push right then left so left is processed first)
                stack.extend([curr.right, curr.left])

        # Return the root of the inverted tree
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