
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Create a new TreeNode with the given value
        new_node = TreeNode(val)

        # If the tree is empty, the new node becomes the root
        if not root:
            return new_node

        # Start traversing from the root
        current = root
        while True:
            # If the value to insert is less than the current node's value, go left
            if val < current.val:
                if current.left:
                    # Continue traversing left if the left child exists
                    current = current.left
                else:
                    # If there's no left child, insert the new node here
                    current.left = new_node
                    break
            else:
                # If the value is greater or equal, go right
                if current.right:
                    # Continue traversing right if the right child exists
                    current = current.right
                else:
                    # If there's no right child, insert the new node here
                    current.right = new_node
                    break
        
        # Return the unchanged root of the tree
        return root
    
    
# Helper function to print the tree in-order
def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

# Build a sample tree manually
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

# Insert new value
solution = Solution()
new_root = solution.insertIntoBST(root, 5)

# Print in-order traversal of the updated tree
print("In-order Traversal After Insertion:", inorder_traversal(new_root))