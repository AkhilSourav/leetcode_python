class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for i in range(self.num_vertices):
            print(i, "->", self.adj_list[i])
    
    # BFS
    # Time Complexity: O(V + E) , Space Complexity: O(V)
    # We need to maintain a visited array to keep track of the nodes that have been visited
    def BFS(self, s):
        visited = [False] * self.num_vertices
        visited[s] = True
        queue = []
        queue.append(s)
        
        while queue:
            cur_node = queue.pop(0)
            print(cur_node, end=" ")
            adjacent_nodes = self.adj_list[cur_node]
            # Traverse through all the adjacent nodes of the current node
            for node in adjacent_nodes:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
            
        
edges = [(0,1),(0,2),(1,2),(2,3),(3,1),(3,2)]

num_vertices = max(max(edges)) + 1

g = Graph(num_vertices)

for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print the adjacency list before BFS
g.print_graph()

# Perform BFS
g.BFS(3)