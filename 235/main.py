
# Time: O(h)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Determine which of the two values is smaller and which is larger
        # This helps us compare them easily with the current root's value
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        
        # Loop to traverse the tree iteratively starting from the root
        while root:
            if root.val > large:
                # If the current node's value is greater than both p and q,
                # the LCA must be in the left subtree
                root = root.left
            elif root.val < small:
                # If the current node's value is less than both p and q,
                # the LCA must be in the right subtree
                root = root.right
            else:
                # The current node is between p and q (inclusive), so it must be the LCA
                return root
        
        # If we reach here, there's no LCA (edge case, usually shouldn't happen in valid BST input)
        return None
    
    
# Build example BST:
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7 9
#       / \
#      3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Create references to the two nodes we're finding the LCA for
p = root.right             # Node with value 8
q = root.left.right       # Node with value 4

# Find and print the LCA
sol = Solution()
lca = sol.lowestCommonAncestor(root, p, q)
print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {lca.val}")