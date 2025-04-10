

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
        
# Time: O(Vertices + Edges)
# Space: O(V)
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If the input node is None, return None (empty graph case)
        if not node:
            return node
        
        # Initialize a queue for BFS traversal
        queue = deque()
        
        # Dictionary to keep track of cloned nodes
        # Key: original node value, Value: new cloned node
        clones = {node.val: Node(node.val)}
        
        # Start BFS with the input node
        queue.append(node)
        
        # Perform BFS traversal
        while queue:
            curr = queue.popleft()  # Get the current node from the queue
            curr_clone = clones[curr.val]  # Get the corresponding cloned node
            
            # Iterate through all neighbors of the current node
            for neighbor in curr.neighbors:
                # If the neighbor hasn't been cloned yet
                if neighbor.val not in clones:
                    # Clone it and store in the dictionary
                    clones[neighbor.val] = Node(neighbor.val)
                    # Add the original neighbor to the queue to visit its neighbors later
                    queue.append(neighbor)
                
                # Add the cloned neighbor to the current clone's neighbors list
                curr_clone.neighbors.append(clones[neighbor.val])
        
        # Return the clone of the input node, which is the entry point to the cloned graph
        return clones[node.val]
    
    
    
# Helper function to print a graph (for verification)
def printGraph(node):
    visited = set()
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        print(f"Node {curr.val} -> {[n.val for n in curr.neighbors]}")
        for neighbor in curr.neighbors:
            stack.append(neighbor)
        
        
# Example Usage:
# Creating a sample graph:
#     1 -- 2
#     |    |
#     4 -- 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Running the function
sol = Solution()
cloned_graph = sol.cloneGraph(node1)

# Printing original and cloned graph
print("Original Graph:")
printGraph(node1)

print("\nCloned Graph:")
printGraph(cloned_graph)