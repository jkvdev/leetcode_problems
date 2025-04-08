
from typing import Optional 
from collections import deque

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Initialize a queue for Breadth-First Search (BFS)
        queue = deque([root])
        # Create a set to store the values we've already seen
        num_set = set()

        # Start BFS traversal
        while queue:
            node = queue.popleft()  # Take the next node from the queue

            # Check if the complement (k - node.val) has already been seen
            if (k - node.val) in num_set:
                return True  # Found two numbers that add up to k
            else:
                # Add current node's value to the set
                num_set.add(node.val)

                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # If no such pair is found, return False
        return False
    
    
# Example: Build a simple binary search tree
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(6, None, TreeNode(7))

# Test the function
sol = Solution()
k = 9  # Example: looking for two nodes that sum to 9 (e.g., 2 + 7)
print(sol.findTarget(root, k))  # Output: True