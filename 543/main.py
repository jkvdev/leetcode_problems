
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Stack for post-order traversal; stores tuples of (node, visited)
        stack = [(root, False)]
        # Dictionary to store the height of each subtree once processed
        max_height_dict = {}
        # Variable to track the maximum diameter found so far
        diameter = 0

        # Start iterative post-order traversal
        while stack:
            node, visited = stack.pop()

            if not visited:
                # First time seeing this node — push it back as visited
                stack.append((node, True))
                
                # Add children to stack (they'll be processed before the current node)
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))

            else:
                # Node has been visited, so calculate its left and right heights
                # If left or right is None, height is 0; otherwise get stored height
                left_height = max_height_dict.pop(node.left, 0)
                right_height = max_height_dict.pop(node.right, 0)

                # The diameter through the current node is the sum of left and right heights
                diameter = max(diameter, left_height + right_height)

                # Store the height of the current node for its parent to use
                max_height_dict[node] = max(left_height, right_height) + 1

        return diameter
    
    
    
# Sample Tree Construction
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Run the code
sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3