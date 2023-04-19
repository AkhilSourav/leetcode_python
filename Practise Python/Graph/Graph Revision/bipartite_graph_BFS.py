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


def check_bipartite_using_bfs(graph, source, color_arr):
    color_arr[source] = 1
   
    queue = []
    queue.append(source)

    while queue:
        cur_node = queue.pop(0)
        adjacent_nodes = graph.adj_list[cur_node]
        
        for node in adjacent_nodes:
            # If the adjacent node is not colored, color it with the opposite color
            if color_arr[node] == -1:
                    color_arr[node] = not color_arr[cur_node]
                    queue.append(node)
            else:
                # If the adjacent node is already colored and its color is same as the current node, 
                # then the graph is not bipartite
                if color_arr[node] == color_arr[cur_node]:
                    return False
    return True


def is_bipartite(graph):
    color_arr = [-1] * graph.num_vertices
    
    for i in range(graph.num_vertices):
        if color_arr[i] == -1:
            if check_bipartite_using_bfs(graph, i, color_arr) == False:
                return False
    return True



edges = [(1,2),(2,6),(2,3),(3,4),(4,5),(5,6),(4,7),(7,8)]
# edges = [(0,1),(1,2),(2,3),(3,0)]

num_vertices = max(max(edges)) + 1

graph = Graph(num_vertices)

for edge in edges:
    graph.add_edge(edge[0], edge[1])

is_bipartite(graph)

print(f"Is the graph bipartite? {is_bipartite(graph)}")