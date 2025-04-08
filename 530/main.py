
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Initialize the minimum difference to infinity — will be updated during traversal
        min_diff = float('inf')
        # prev_val keeps track of the value of the previously visited node
        # Start with negative infinity to handle the first comparison
        prev_val = float('-inf')
        # Stack to help us perform iterative in-order traversal
        stack = []

        # Main loop runs as long as we have a node to process or the stack isn't empty
        while root or stack:
            if root:
                # Go as far left as possible, pushing nodes onto the stack
                stack.append(root)
                root = root.left
            else:
                # No more left children, process the node at the top of the stack
                root = stack.pop()
                # Update the minimum difference using the current node and previous value
                # (in-order traversal ensures ascending order in BST)
                min_diff = min(min_diff, root.val - prev_val)
                # Update prev_val to the current node's value before moving to the right
                prev_val = root.val
                # Move to the right child to continue in-order traversal
                root = root.right

        # Return the smallest difference found between any two adjacent nodes in in-order traversal
        return min_diff
    
    
# Example BST:
#     4
#    / \
#   2   6
#  / \
# 1   3

# Build the tree
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6)

# Run the solution
sol = Solution()
result = sol.getMinimumDifference(root)
print("Minimum Absolute Difference:", result)