class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # For a directed graph, we only add an edge from u to v    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)


def topoSort(graph):
    safe_nodes = []
    # Create a list to store the in-degree of each vertex
    in_degree = [0] * graph.num_vertices
    # Create a queue to store the vertices with in-degree 0
    q = []
    
    # Calculate the in-degree of each vertex
    for i in range(graph.num_vertices):
        for node in graph.adj_list[i]:
            in_degree[node] += 1
    
    # Add all the vertices with in-degree 0 to the queue
    for i in range(graph.num_vertices):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        cur_node = q.pop(0)
        safe_nodes.append(cur_node)
        
        # Reduce the in-degree of all the adjacent vertices of the current node by 1
        # If any of the adjacent vertices have in-degree 0, add them to the queue
        for node in graph.adj_list[cur_node]:
            in_degree[node] -= 1
            
            if in_degree[node] == 0:
                q.append(node)
    
    # Sort the safe nodes
    safe_nodes.sort()
    return safe_nodes

edges = [[5,0],[5,2],[4,0],[2,3],[3,1],[4,1]]

# edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(3,7),(7,5),(8,2),(8,9),(9,10),(10,8)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

# Reverse the edges
for edge in edges:
    graph.add_edge(edge[1], edge[0])

"""
NOTE:
We are reversing the edges and then finding the topological sort of the graph.
We are reversing the graph because,
Initially the terminal nodes are those who have out_degree 0 
but after reversal the terminal nodes becomes those which have in_degree 0 
so we can apply Kahn's algo to find all the nodes connected to it also, 
path containing cycle will not be included in the topological sort.
"""

print(f"Safe states are: {topoSort(graph)}")