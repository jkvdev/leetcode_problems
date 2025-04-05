
from collections import deque
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the current node is None (i.e., empty tree or leaf child), return 0
        if not root:
            return 0

        # If at least one child is None, we need to consider the depth of the non-null child only
        # This handles cases like skewed trees or incomplete trees
        if None in [root.left, root.right]:
            # We use max(...) here because if one side is None, its depth is 0
            # So we only consider the depth of the non-null child
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            # If both children exist, return the minimum depth of either subtree
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# === Test the function ===

# Example binary tree:
#       1
#      / \
#     2   3
#    /
#   4

# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3)

# Create Solution instance and call minDepth
solution = Solution()
print(solution.minDepth(root))  # Output: 2 (1 -> 3 is the shortest path to a leaf)
