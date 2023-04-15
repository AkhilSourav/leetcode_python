class Graph:
    # Constructor
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # Add an edge from u to v
    # Since this is an undirected graph, add an edge from v to u as well
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    # Print the adjacency list representation of the graph
    def print_graph(self):
        for i in range(self.num_vertices):
            print(i, "->", self.adj_list[i])

# Given the list of edges of a graph, create an adjacency list            
edges = [(0,1),(0,2),(2,1),(2,3)]

# Get the number of vertices in the graph
num_vertices = max(max(edges)) + 1

# Create an empty adjacency list
g = Graph(num_vertices)

# Interate over the edges and add them to the graph
for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print the adjacency list
g.print_graph()
