
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
        # Start from the root of the Binary Search Tree
        current_node = root
        
        # Traverse the tree iteratively until the node is found or until there are no more nodes
        while current_node:
            # If the current node's value matches the target value, return the node
            if current_node.val == val:
                return current_node
            # If the target value is greater than the current node's value,
            # move to the right subtree (since in BST, right children are greater)
            elif current_node.val < val:
                current_node = current_node.right
            # If the target value is less than the current node's value,
            # move to the left subtree (since in BST, left children are smaller)
            else:
                current_node = current_node.left
                
        # If we exit the loop, the value was not found in the tree
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
    