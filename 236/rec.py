
from collections import deque

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the root is None or if the root is either of the nodes (p or q), return the root
        if root == None or root == p or root == q:
            return root
        
        # Recursively search for the LCA in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively search for the LCA in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right subtrees return a node, this means p and q are found
        # in different subtrees, so the current node is the LCA
        if left != None and right != None:
            return root
        
        # If only the left subtree has a non-null result, return the node from the left subtree
        if left != None:
            return left
        
        # If only the right subtree has a non-null result, return the node from the right subtree
        return right
      
      
      
# Build a sample binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Nodes to find LCA for
p = root.left.left  # Node 6
q = root.left.right.right  # Node 4

# Run the function
sol = Solution()
lca = sol.lowestCommonAncestor(root, p, q)
print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {lca.val}")