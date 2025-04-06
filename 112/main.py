
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
        # If the tree is empty, there can be no path that adds to targetSum
        if not root:
            return False 
        
        # Initialize a stack for DFS traversal. Each item is a tuple of (node, current path sum)
        stack = [(root, root.val)]
        
        # Continue traversing while there are nodes left to visit (DFS)
        while stack: 
            # Get the current node and the sum of the path that led to it
            curr, val = stack.pop()
            
            # Check if the current node is a leaf (no children) 
            # and if the path sum equals the target sum
            if (not curr.left and not curr.right and val == targetSum):
                return True  # A valid path has been found
            
            # If the right child exists, add it to the stack with updated path sum
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            
            # If the left child exists, add it to the stack with updated path sum
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        
        # If the loop ends with no valid path found, return False
        return False
    
    
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