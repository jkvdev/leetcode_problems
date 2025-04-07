
from typing import Optional

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter found so far
        self.diameter = 0

        # Helper function to compute the depth (height) of the tree recursively
        def depth(root):
            # Base case: If the node is None, its depth is 0
            if not root:
                return 0
            
            # Recursively compute the depth of the left and right subtrees
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            
            # Update the diameter if the path through this node is larger
            # The diameter at this node is the sum of left and right depths
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the height of the current node (1 + max of left and right subtree heights)
            return 1 + max(left_depth, right_depth)

        # Start the recursion from the root
        depth(root)
        # Return the maximum diameter found
        return self.diameter
    
    
    
# Sample Tree Construction
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Run the code
sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3