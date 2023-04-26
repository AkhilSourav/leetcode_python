class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # For a directed graph, we only add an edge from u to v    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)




def topoSort(graph):
    count = 0
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
        count += 1
        
        # Reduce the in-degree of all the adjacent vertices of the current node by 1
        # If any of the adjacent vertices have in-degree 0, add them to the queue
        for node in graph.adj_list[cur_node]:
            in_degree[node] -= 1
            
            if in_degree[node] == 0:
                q.append(node)
    
    if count != graph.num_vertices:
        return True
    return False




edges = [(0,1),(1,2),(2,0),(3,4),(4,5)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

for edge in edges:
    graph.add_edge(edge[0], edge[1])

""" 
NOTE: 
We are using the same topoSort function as in topological_sort_bfs_kahns_algorithm.py
but we are just modifying the return statement to return True if count == graph.num_vertices
since TopoSort is only possible for a DAG and if there is a cycle in the graph, then the count
will not be equal to the number of vertices in the graph.
"""
print(f"Does the given directed graph have a cycle: {topoSort(graph)}")