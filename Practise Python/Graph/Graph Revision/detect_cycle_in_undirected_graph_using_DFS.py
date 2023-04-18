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


def detect_cycle_DFS(i, parent, graph, visited):
    visited[i] = True
    adjacent_nodes = graph.adj_list[i]
    
    for node in adjacent_nodes:
        if visited[node] == False:
            new_parent = i
            # If we observe carefully here, at any point during recursion if we want to
            # return something from the function, then return is called twice.
            if detect_cycle_DFS(node, new_parent, graph, visited) == True:
                return True
        elif parent != node:
            return True
    return False
    



def check_for_cycle(g):
    num_vertices = g.num_vertices
    visited = [False] * num_vertices
    
    for i in range(num_vertices):
        if visited[i] == False:
            if detect_cycle_DFS(i, -1, g, visited) == True:
                return True
            else:
                return False



# Given the list of edges of a graph, create an adjacency list            
edges = [(0,1),(0,2),(2,1),(3,0),(2,4)]

""" Note : Below code is failing bcoz 
max(edges) is returning (3,0) and max(max(edges) + 1) is returning 4

It should return 5, since the graph has 5 vertices
"""
# # Get the number of vertices in the graph
# num_vertices = max(max(edges)) + 1

# Create an empty adjacency list
g = Graph(5)

# Iterate over the edges and add them to the graph
for edge in edges:
    g.add_edge(edge[0], edge[1])
    



print(f"Graph contains cycle: {check_for_cycle(g)}")