
from typing import Optional, List
from collections import deque

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the input array is empty, return None
        if not nums: 
            return None
        
        # Get the length of the array and calculate the middle index
        n = len(nums)
        mid = n // 2
        
        # Create the root node of the BST using the middle element
        root = TreeNode(nums[mid])
        
        # Initialize a queue to keep track of nodes to be processed.
        # Each element in the queue is a tuple: (parent node, left index, right index)
        q = deque()
        # Add left half of the array (for root's left child)
        q.append((root, 0, mid - 1))
        # Add right half of the array (for root's right child)
        q.append((root, mid + 1, n - 1))
        
        # Process nodes in the queue
        while q:
            parent, left, right = q.popleft()
            
            # Only proceed if the current sub-array is valid
            if left <= right:
                # Find the middle index of the current sub-array
                mid = (left + right) // 2
                # Create a child node using the middle element
                child = TreeNode(nums[mid])
                
                # Attach the child node to the parent appropriately
                if nums[mid] < parent.val:
                    parent.left = child  # If less than parent, go to left
                else:
                    parent.right = child  # Otherwise, go to right
                
                # Add the left and right sub-ranges of the current child node to the queue
                q.append((child, left, mid - 1))      # For child's left subtree
                q.append((child, mid + 1, right))     # For child's right subtree
        
        # Return the root of the constructed BST
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