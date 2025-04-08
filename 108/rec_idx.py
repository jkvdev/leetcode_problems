

from typing import Optional, List
from collections import deque

# Time: O(n)
# Space: O(log n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Helper function that builds the BST from nums[left:right+1]
        def convert(left, right):
            # Base case: if the left index exceeds the right, there's nothing to process
            if left > right:
                return None
            
            # Choose the middle index to keep the tree balanced
            mid = (left + right) // 2
            # Create a TreeNode using the middle element
            node = TreeNode(nums[mid])
            # Recursively build the left subtree using the left half
            node.left = convert(left, mid - 1)
            # Recursively build the right subtree using the right half
            node.right = convert(mid + 1, right)
            
            # Return the current node (root of the current subtree)
            return node
        
        # Start recursion from the full array range
        return convert(0, len(nums) - 1)
    
# Function to print tree in-order (left-root-right)
def print_in_order(node):
    if node:
        print_in_order(node.left)
        print(node.val, end=' ')
        print_in_order(node.right)


nums = [-10, -3, 0, 5, 9]
sol = Solution()
bst_root = sol.sortedArrayToBST(nums)

print("In-order traversal of the resulting BST:")
print_in_order(bst_root)