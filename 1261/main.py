
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# Time: O(N)
# Space: O(N)
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        """
        Constructor: Recovers the contaminated binary tree by assigning correct values.
        - The root of the tree is set to 0.
        - Uses a helper function `recover_binary_tree` to restore all node values.
        - Stores recovered values in a set for fast lookup.
        """
        self.node_values = set()  # Store all valid node values for O(1) lookup.
        
        if root:
            root.val = 0  # The root is always set to 0.
            self.node_values.add(0)  # Add root's value to the set.
            self.recover_binary_tree(root.left, 1)  # Restore the left subtree.
            self.recover_binary_tree(root.right, 2) # Restore the right subtree.

    def recover_binary_tree(self, curr: TreeNode, val: int):
        """
        Recursively restores the tree using the given formula:
        - Left child of a node with value x: 2 * x + 1
        - Right child of a node with value x: 2 * x + 2
        """
        if not curr:
            return  # Base case: Stop if the node is None.

        curr.val = val  # Assign the correct value to the current node.
        self.node_values.add(val)  # Store the value in the set for quick lookup.

        # Recursively recover the left and right subtrees.
        self.recover_binary_tree(curr.left, 2 * val + 1)
        self.recover_binary_tree(curr.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        """
        Checks if a given value exists in the recovered tree.
        - Returns True if the target is in the set, otherwise False.
        - O(1) time complexity due to set lookup.
        """
        return target in self.node_values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# Create a contaminated binary tree (all values set to -1)
# Example:
#       -1
#      /   \
#    -1     -1
#   /  \   /  \
# -1   -1 -1  -1
root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.right = TreeNode(-1)

# Instantiate the FindElements class
find_elements = FindElements(root)

# Test the `find` method
print(find_elements.find(2))  # Output: True  (since 2 should exist in the recovered tree)
print(find_elements.find(5))  # Output: True  (5 should exist)
print(find_elements.find(10)) # Output: False (10 is not in the tree)