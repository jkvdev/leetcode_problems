
from typing import Optional, List
from collections import deque

# Time: O(n^2)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the list is empty, return None (no node to create)
        if not nums:
            return None
        
        # Find the middle index of the current list
        mid = len(nums) // 2
        # Create the root node using the middle element
        root = TreeNode(nums[mid])
        
        # Recursively build the left subtree using the left half of the list
        root.left = self.sortedArrayToBST(nums[:mid])
        # Recursively build the right subtree using the right half of the list
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        # Return the root node of the subtree (or full tree, if top level)
        return root 
    
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