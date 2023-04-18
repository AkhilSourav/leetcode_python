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



def detect_cycle( i ,graph, visited):
    visited[i] = True
    queue = []
    queue.append((i,-1))
    
    while queue:
        cur_node, parent = queue.pop(0)
        adjacent_nodes = graph.adj_list[cur_node]
        
        for node in adjacent_nodes:
            if visited[node] == False:
                visited[node] = True
                queue.append((node, cur_node))
        # While traversing, If someone is visiting a node which is already visited and 
        # it is not the parent of the current node then there is a cycle.
            elif parent != node:
                return True
    return False
    


def check_for_cycle(g):
    num_vertices = g.num_vertices
    visited = [False] * num_vertices
    
    for i in range(num_vertices):
        if visited[i] == False:
            if detect_cycle(i,g, visited) == True:
                return True
            else:
                return False



# Given the list of edges of a graph, create an adjacency list            
edges = [(0,1),(0,2),(3,0),(2,4)]

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