
# Time: O(V + E)
# Space: O(V)

# Create a graph and traverse it with BFS and DFS
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty adjacency list (dictionary)

    # Add edges
    def add(self, from_vertex, to_vertex):
        # Add both directions since it's an undirected graph
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        if to_vertex not in self.graph:
            self.graph[to_vertex] = []
        self.graph[from_vertex].append(to_vertex)
        self.graph[to_vertex].append(from_vertex)

    # Count the number of edges in the graph
    def count_edges(self):
        edge_count = 0  # Initialize a counter for total edges

        # Loop through each vertex in the graph
        for vertex in self.graph:
            # Add the number of edges (neighbors) from this vertex
            edge_count += len(self.graph[vertex])

        return edge_count // 2  # Return the total number of edges (for undirected, it's double-counted)

    # Find a cycle
    def dfs(self, start_vertex):
        # If the starting vertex is not in the graph, return False
        if start_vertex not in self.graph:
            return False

        stack = [(start_vertex, -1)]  # Stack holds (current_vertex, parent_vertex)
        visited = set()               # Keep track of visited nodes

        while stack:
            vertex, parent = stack.pop()  # Get the current vertex and its parent

            if vertex in visited:
                # If the node is already visited, a cycle is detected
                return True

            visited.add(vertex)  # Mark the current node as visited

            # Iterate through all neighbors of the current vertex
            for neighbor in self.graph.get(vertex, []):
                # Don't revisit the parent node (in undirected graph)
                if neighbor != parent:
                    stack.append((neighbor, vertex))  # Add neighbor with current as parent

        # If the loop finishes with no repeated visits, there's no cycle
        return False

    # Find largest node
    def findLargestNode(self, start_vertex):
        # Check if the start node exists in the graph
        if start_vertex not in self.graph:
            return None

        queue = [start_vertex]       # Initialize BFS queue with the starting vertex
        traversal = []               # Track visited nodes to avoid processing them again
        largest_node = start_vertex  # Store the largest node value found so far

        while queue:  # Loop while there are nodes to process in the queue
            vertex = queue.pop(0)  # Pop the first element (FIFO for BFS)

            if vertex not in traversal:  # If the node hasn't been visited
                traversal.append(vertex)  # Mark it as visited

                if vertex > largest_node:  # Compare current node with the largest found
                    largest_node = vertex  # Update the largest node if current is greater

                if vertex in self.graph:
                    queue.extend(self.graph[vertex])  # Add neighbors to the queue

        return largest_node  # Return the largest node value found during BFS


# Example usage:
g = Graph()
g.add(1, 2)
g.add(2, 3)
g.add(3, 4)
g.add(4, 1)  # This edge introduces a cycle

print("Largest node:", g.findLargestNode(1))  # Output: Largest node: 4

print("Cycle detected?" , g.dfs(1))  # Output: Cycle detected? True

print("Number of edges:", g.count_edges())  # Output: Number of edges: 3