
from typing import Optional

# Time: O(n)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Traverse the tree iteratively
        while root:
            # If the current node's value matches the search value, return the node
            if root.val == val:
                return root
            # If the value to find is greater, move to the right subtree
            elif root.val < val:
                root = root.right
            # If the value to find is smaller, move to the left subtree
            else:
                root = root.left
        # If the value was not found, return None
        return None
    


# Helper function to print a subtree (for display purposes)
def print_subtree(node):
    if not node:
        return "None"
    return f"TreeNode({node.val}, left={print_subtree(node.left)}, right={print_subtree(node.right)})"


# Create a sample BST:
#         4
#        / \
#       2   7
#      / \
#     1   3

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7)

solution = Solution()
result = solution.searchBST(root, 7)

# Print the result subtree rooted at the node with value 2
print(print_subtree(result))
    