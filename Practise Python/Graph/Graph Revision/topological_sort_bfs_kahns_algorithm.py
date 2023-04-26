class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # For a directed graph, we only add an edge from u to v    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)




def topoSort(graph):
    topoSorted_List = []
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
        topoSorted_List.append(cur_node)
        
        # Reduce the in-degree of all the adjacent vertices of the current node by 1
        # If any of the adjacent vertices have in-degree 0, add them to the queue
        for node in graph.adj_list[cur_node]:
            in_degree[node] -= 1
            
            if in_degree[node] == 0:
                q.append(node)
    
    return topoSorted_List




edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

for edge in edges:
    graph.add_edge(edge[0], edge[1])


print(f"Topological Sort for the given graph is: {topoSort(graph)}")