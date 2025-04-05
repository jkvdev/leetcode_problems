
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the tree is empty (root is None), depth is 0.
        if not root:
            return 0
        
        # Recursively compute the depth of the left and right subtrees.
        # The depth of the current node is 1 (for itself) plus 
        # the max of left and right subtree depths.
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1

# Creating a sample binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Running the function
sol = Solution()
print(sol.maxDepth(root))  # Output: 3
