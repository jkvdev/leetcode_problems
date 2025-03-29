from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Get the total number of nodes in postorder traversal
        N = len(postorder)

        # Create a dictionary to map each node value to its index in postorder
        post_val_to_idx = {}  # (value -> index)
        for i, n in enumerate(postorder):  
            post_val_to_idx[n] = i  # Store the index of each value in postorder

        # Recursive function to construct the binary tree 
        def build(i1, i2, j1):
            # Base case: if start index exceeds end index, 
            # return None (no node to process)
            if i1 > i2:
                return None

            # Create the root node with the current value from preorder traversal
            root = TreeNode(preorder[i1])

            # If there is more than one node, 
            # construct left and right subtrees
            if i1 != i2:
                # Get the value of the left child from preorder
                left_val = preorder[i1 + 1]
                # Find its index in postorder to determine subtree boundaries
                mid = post_val_to_idx[left_val]

                # Calculate the size of the left subtree
                left_size = mid - j1 + 1

                # Recursively construct the left subtree
                root.left = build(i1 + 1, i1 + left_size, j1)
                # Recursively construct the right subtree
                root.right = build(i1 + left_size + 1, i2, mid + 1)

            # Return the constructed subtree
            return root

        # Call the recursive function to build the entire tree and return its root
        return build(0, N - 1, 0)
    
    
# Function to print the tree (for debugging purposes)
def print_tree(root):
    if not root:
        return "None"
    left = print_tree(root.left)
    right = print_tree(root.right)
    return f"{root.val} -> ({left}, {right})"

# Example input
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

# Run the function
solution = Solution()
root = solution.constructFromPrePost(preorder, postorder)

# Print the tree structure
print(print_tree(root))