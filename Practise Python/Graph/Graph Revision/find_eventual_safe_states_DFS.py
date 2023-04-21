class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    # For a directed graph, we only add an edge from u to v    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

def detect_cycle_using_dfs(cur_node, visited, path_visited, safe_states, graph):
    visited[cur_node] = True
    path_visited[cur_node] = True
    # NEW CHANGE
    safe_states[cur_node] = False
    adjacent_nodes = graph.adj_list[cur_node]
    
    for node in adjacent_nodes:
        if visited[node] == False:
            if detect_cycle_using_dfs(node, visited, path_visited, safe_states, graph) == True:
                return True
        elif path_visited[node] == True:
            return True

    # Backtracking Step
    path_visited[cur_node] = False
    # NEW CHANGE
    safe_states[cur_node] = True
    return False


def check_for_cycle(graph):
    
    visited = [False] * graph.num_vertices
    # This is used to track the path that we are traversing
    # If the node is already visited and its in the same path, then we have a cycle
    path_visited = [False] * graph.num_vertices
    
    # NEW CHANGE
    # This is used to track the safe states
    safe_states = {i:False for i in range(graph.num_vertices)}
    
    for i in range(graph.num_vertices):
        if visited[i] == False:
            detect_cycle_using_dfs(i, visited, path_visited, safe_states, graph)  
    
    for i in range(graph.num_vertices):
        # NEW CHANGE
        if safe_states[i] == True:
            print(i, end=" ")



# edges = [[5,0],[5,2],[4,0],[2,3],[3,1],[4,1]]

edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(3,7),(7,5),(8,2),(8,9),(9,10),(10,8)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

for edge in edges:
    if edge:
        graph.add_edge(edge[0], edge[1])


""" 
Note: Detecting cycle in a directed graph is different from detecting cycle in an undirected graph.
        So, we can't use the same logic here as we used in the undirected graph.
"""
        
check_for_cycle(graph)
