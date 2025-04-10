
# Time: O(V + E)
# Space: O(V)

# Create a graph and traverse it with BFS and DFS
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty adjacency list (dictionary)

    # Add edges
    def add(self, from_vertex, to_vertex):
        # Add an edge from from_vertex to to_vertex
        if from_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            self.graph[from_vertex] = [to_vertex]

    # DFS traversal
    def dfs(self, start_vertex):
        # Check if the starting vertex exists in the graph
        if start_vertex not in self.graph:
            return []  # Return an empty list if the vertex doesn't exist

        stack = [start_vertex]       # Use a stack to track the path (LIFO order)
        traversal = []               # Store the DFS traversal result here

        # Explore the graph
        while stack:
            vertex = stack.pop()     # Pop the most recent vertex added

            if vertex not in traversal:     # If the vertex hasn't been visited yet
                traversal.append(vertex)    # Add it to the traversal list

                # Add neighbors to the stack in reverse order to maintain left-to-right order
                if vertex in self.graph:
                    stack.extend(reversed(self.graph[vertex]))

        return traversal  # Return the final DFS traversal result

    # BFS traversal
    def bfs(self, start_vertex):
        # Check if the start_vertex exists in the graph
        if start_vertex not in self.graph:
            return []  # If it doesn't exist, return an empty list

        queue = [start_vertex]       # Initialize the queue with the starting vertex
        traversal = []               # List to store the BFS traversal result

        while queue:                 # Keep looping until the queue is empty
            vertex = queue.pop(0)    # Remove the first vertex from the queue (FIFO)

            if vertex not in traversal:  # If it hasn't been visited yet
                traversal.append(vertex)  # Mark it as visited (add to traversal list)

                # Add all adjacent (neighboring) vertices to the queue
                if vertex in self.graph:
                    queue.extend(self.graph[vertex])

        return traversal  # Return the BFS order




# Create a graph object
g = Graph()

# Add edges to build the graph
g.add('A', 'B')
g.add('A', 'C')
g.add('B', 'D')
g.add('C', 'E')
g.add('D', 'F')
g.add('E', 'F')

# Perform BFS starting from vertex 'A'
result1 = g.bfs('A')

# Print the result
print("BFS Traversal:", result1)

# Run DFS starting from vertex 'A'
result2 = g.dfs('A')

# Print the DFS traversal result
print("DFS Traversal:", result2)