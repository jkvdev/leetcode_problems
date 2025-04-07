
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
        # Initialize a queue for BFS traversal and a dictionary to store each node's parent
        queue = deque([root])
        parent = {root: None}  # The root has no parent

        # Continue BFS until we have found both p and q in the parent map
        while queue:
            node = queue.popleft()

            # If left child exists, add it to the queue and record its parent
            if node.left:
                queue.append(node.left)
                parent[node.left] = node

            # If right child exists, add it to the queue and record its parent
            if node.right:
                queue.append(node.right)
                parent[node.right] = node

            # If we've found both p and q, we can stop the search
            if p in parent and q in parent:
                break

        # Create a set to store all ancestors of node p
        ancestors = set()
        # Traverse up from p to the root and add all ancestors to the set
        while p:
            ancestors.add(p)
            p = parent[p]
        # Traverse up from q to the root. The first ancestor that appears in p's ancestor set is the LCA
        while q:
            if q in ancestors:
                return q
            q = parent[q]
      
      
      
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