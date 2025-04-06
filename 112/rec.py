
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, return False
        if not root:
            return False
        
        # If we reach a leaf node, check if the remaining targetSum equals the node's value
        if (not root.left and not root.right 
            and targetSum == root.val):
            return True 
        
        # Recur on left and right children with the updated targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
    
    
# Build the binary tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1

root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

# Create Solution object
sol = Solution()

# Call the function with target sum = 22
print(sol.hasPathSum(root, 22))  # Output: True