
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
        # Edge case check
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Each item is a tuple: (node, depth)
        
        # Initiate BFS
        while queue:
            node, level = queue.popleft()
            
            # If this is a leaf node, return its depth
            if not node.left and not node.right:
                return level
            
            # Add left child if it exists
            if node.left:
                queue.append((node.left, level + 1))
            
            # Add right child if it exists
            if node.right:
                queue.append((node.right, level + 1))
        
        return 0  # Fallback, shouldn't reach here

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
