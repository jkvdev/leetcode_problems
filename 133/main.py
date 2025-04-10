
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
# Time: O(Vertices + Edges)
# Space: O(V)
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None  # If the input graph is empty, return None
        
        start = node  # Store the reference to the original start node
        old_to_new = {}  # Dictionary to map old nodes to their cloned versions
        stack = [start]  # Stack for depth-first search (DFS) traversal
        visited = set()  # Set to track visited nodes
        visited.add(start)  # Mark the start node as visited
        
        # Step 1: Clone all nodes and store them in the dictionary
        while stack:
            node = stack.pop()  # Get the current node from the stack
            old_to_new[node] = Node(val=node.val)  # Create a new node with the same value
            
            # Traverse its neighbors
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    stack.append(neighbor)  # Add to stack for further exploration
        
        # Step 2: Clone the edges (neighbors)
        for old_node, new_node in old_to_new.items():
            for neighbor in old_node.neighbors:  # Go through the original node's neighbors
                new_neighbor = old_to_new[neighbor]  # Find the cloned neighbor node
                new_node.neighbors.append(new_neighbor)  # Add the cloned neighbor to the new node
        
        return old_to_new[start]  # Return the cloned version of the start node
    
    
    
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