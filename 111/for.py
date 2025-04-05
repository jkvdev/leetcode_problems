
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
        # Edge case check: If the root is None, return 0 as the tree is empty
        if not root:
            return 0
        
        # Initialize a queue for BFS and add the root node to it
        queue = deque([root])  # Using deque for efficient popping from the front
        level = 0  # Variable to track the depth of the tree (level in BFS)
        
        # Initiate BFS to explore the tree level by level
        while queue:
            level += 1  # Increment depth level as we go down the tree
            
            # Process all nodes at the current level
            for i in range(len(queue)):
                
                # Dequeue a node (i.e., get the first node in the queue)
                node = queue.popleft()
                
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
                    
                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                
                # If we encounter a leaf node (no left and right children), return its depth
                if not node.left and not node.right:
                    return level  # This is the minimum depth since BFS explores level by level
        
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
