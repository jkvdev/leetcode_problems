from collections import deque

# Time: O(n)
# Space: O(n)

# Step 1: Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 2: Define the function
def largest_node_binary_tree(root):
    # Initialize a queue for level-order traversal (starting with the root)
    queue = deque([root])
    # Set initial max_node to the smallest possible value so any node will be larger
    max_node = float('-inf')
    
    # Traverse the tree level by level
    while queue:
        # Remove the node from the front of the queue
        curr_node = queue.popleft()
        
        # Update max_node if the current node's value is greater
        if curr_node.val > max_node:
            max_node = curr_node.val
        
        # Add the left child to the queue if it exists
        if curr_node.left:
            queue.append(curr_node.left)
        
        # Add the right child to the queue if it exists
        if curr_node.right:
            queue.append(curr_node.right)
    
    # Return the largest value found in the tree
    return max_node

# Step 3: Create a sample tree
# Example Tree:
#        10
#       /  \
#      5    15
#          / \
#         12  20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

# Step 4: Run the function
print(largest_node_binary_tree(root))  # Output: 20