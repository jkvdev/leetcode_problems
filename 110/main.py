
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use a list to store a single boolean value (mutable object)
        balanced = [True]  
        
        def height(root):
            # Base case: if node is None, return height as 0
            if not root:
                return 0
              
            # Recursively compute the height of the left and right subtrees
            left = height(root.left)
            right = height(root.right)
            
            # Check if the current node causes imbalance
            if abs(left - right) > 1:
                balanced[0] = False  # Mark tree as unbalanced
                return 0  # Early return (height is no longer relevant)

            # Return the height of the current node (1 + max subtree height)
            return 1 + max(left, right)
          
        # Start the height calculation from the root
        height(root)
        # Return whether the tree is balanced or not
        return balanced[0]

# Tree Structure:
#       1
#      / \
#     2   3
#    / \
#   4   5
root_balanced = TreeNode(1)
root_balanced.left = TreeNode(2)
root_balanced.right = TreeNode(3)
root_balanced.left.left = TreeNode(4)
root_balanced.left.right = TreeNode(5)

sol = Solution()
print(sol.isBalanced(root_balanced))  # Output: True

# Tree Structure:
#       1
#      / 
#     2   
#    / 
#   3   
root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.left.left = TreeNode(3)

sol = Solution()
print(sol.isBalanced(root_unbalanced))  # Output: False
