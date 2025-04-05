
from collections import deque
from typing import Optional, List

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Initialize a queue with the root node to do level-order traversal (BFS)
        queue = deque([root])
        # This will hold the average of each level
        result = []
        
        # Traverse the tree level by level
        while queue:
            level = []  # List to hold values of nodes at the current level
            
            # Iterate over all nodes at the current level
            for i in range(len(queue)):
                node = queue.popleft()  # Remove node from the front of the queue
                level.append(node.val)  # Add its value to the current level's list
                
                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Compute average of current level and add to result
            result.append(sum(level) / len(level))
        
        # Return the list of averages for each level
        return result
      
      
# -------------------------------
# Example: Create a sample binary tree:
#         3
#        / \
#       9  20
#          / \
#         15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Call the method
solution = Solution()
averages = solution.averageOfLevels(root)

print(averages)  # Output: [3.0, 14.5, 11.0]