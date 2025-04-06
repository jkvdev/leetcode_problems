
from typing import Optional

# Time: O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize a stack with a tuple containing the root nodes of both trees
        stack = [(p, q)]

        # Perform iterative depth-first traversal (DFS)
        while stack:
            # Pop the top pair of nodes (one from each tree)
            node1, node2 = stack.pop()

            # If both nodes are None, continue to next pair (no difference found)
            if not node1 and not node2:
                continue

            # If one node is None or the values don't match, trees are not the same
            elif None in [node1, node2] or node1.val != node2.val:
                return False

            # Add the right children of both nodes to the stack for comparison
            stack.append((node1.right, node2.right))
            # Add the left children of both nodes to the stack for comparison
            stack.append((node1.left, node2.left))

        # If we finish processing all nodes without returning False, the trees are the same
        return True
    
    
# Create example trees
# Tree 1:      1
#            /   \
#           2     3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Tree 2:      1
#            /   \
#           2     3
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Instantiate Solution and check if the trees are the same
sol = Solution()
print(sol.isSameTree(p, q))  # Output: True