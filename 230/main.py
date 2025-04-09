
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # This will simulate the in-order traversal using iteration

        # In-order traversal: left -> node -> right
        # It gives values in ascending order for a BST
        while root or stack:
            # Traverse as far left as possible and push all left nodes to the stack
            if root:
                stack.append(root)
                root = root.left

            else:
                # We've reached the leftmost node, now visit the node
                root = stack.pop()
                k -= 1  # We've visited one more node
                
                # If we've reached the kth visited node, return its value
                if k == 0:
                    return root.val  # This is the kth smallest value in the BST

                # Now, traverse the right subtree
                root = root.right
        
        
# Build the BST
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root.right = TreeNode(6)

# Run the solution
sol = Solution()
k = 3
result = sol.kthSmallest(root, k)
print(f"The {k}rd smallest element is: {result}")