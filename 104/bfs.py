
from collections import deque
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
        
        # Initialize a queue for level-order traversal (BFS)
        # Each element in the queue is a tuple: (node, current depth level)
        queue = deque([(root, 1)])

        # Loop through the queue until it's empty
        while queue:
            # Pop the front of the queue (current node and its level)
            node, level = queue.popleft()

            # If the node has a right child, add it to the queue
            # Increase the level by 1 for the child
            if node.right:
                queue.append((node.right, level + 1))

            # If the node has a left child, add it to the queue
            # Increase the level by 1 for the child
            if node.left:
                queue.append((node.left, level + 1))

        # Once the queue is empty, the `level` variable will hold the maximum depth reached
        return level

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
