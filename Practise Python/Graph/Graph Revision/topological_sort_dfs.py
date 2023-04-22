class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # For a directed graph, we only add an edge from u to v    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)


def topoSortUtil(cur_node, visited, stack, graph):
    visited[cur_node] = True
    
    adjacent_nodes = graph.adj_list[cur_node]
    
    for node in adjacent_nodes:
        if visited[node] == False:
            topoSortUtil(node, visited, stack, graph)
    
    stack.insert(0, cur_node)
    
def topoSort(graph):
    visited = [False] * graph.num_vertices
    stack = []
    
    for i in range(graph.num_vertices):
        if visited[i] == False:
            topoSortUtil(i, visited, stack, graph)
    
    return stack


edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

for edge in edges:
    graph.add_edge(edge[0], edge[1])
    
""" Note: Topological Sort is only possible for a Directed Acyclic Graph (DAG)"""
print(f"Topological Sort for the given graph is: {topoSort(graph)}")