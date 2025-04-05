
from typing import Optional, List
from collections import deque

# Time: O(n)
# Space:O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if root is None:
            return []
        
        # Initialize a queue for BFS traversal, starting with the root node
        queue = deque([root])
        # This will store the final list of levels
        tree = []

        # Continue traversing while there are nodes in the queue
        while queue:
            # Temporary list to store the values of the current level
            level = []

            # Loop over all nodes at the current level
            for i in range(len(queue)):
                # Pop the leftmost node in the queue
                node = queue.popleft()
                
                # Add its value to the current level list
                level.append(node.val)

                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level values to the final result
            tree.append(level)

        # Return the list of level-order values
        return tree
    
    
# Create a sample binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

# Run the level order traversal
sol = Solution()
result = sol.levelOrder(root)
print(result)  # Output: [[1], [2, 3], [4, 5]]