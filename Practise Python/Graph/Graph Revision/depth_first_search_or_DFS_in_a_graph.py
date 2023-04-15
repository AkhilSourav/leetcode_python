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
    
    def DFS(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        adjacent_nodes = self.adj_list[s]
        
        for node in adjacent_nodes:
            if visited[node] == False:
                self.DFS(node, visited)
    
    def DFS_driver_code(self,s):
        visited = [False] * self.num_vertices
        
        self.DFS(s, visited)


edges = [(0,1),(0,2),(1,2),(2,3),(3,1)]

num_vertices = max(max(edges)) + 1

g = Graph(num_vertices)

for edge in edges:
    g.add_edge(edge[0], edge[1])

# Print the adjacency list before DFS
g.print_graph()

# Perform DFS
g.DFS_driver_code(2)