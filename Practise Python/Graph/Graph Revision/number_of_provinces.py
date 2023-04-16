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
        # print(s, end=" ")
        adjacent_nodes = self.adj_list[s]
        
        for node in adjacent_nodes:
            if visited[node] == False:
                self.DFS(node, visited)
    
    def number_of_provinces(self):
        visited = [False] * self.num_vertices
        # Count the number of times DFS is called
        count = 0
        for s in range(self.num_vertices):
            # Handle case for 1 based indexing
            # We dont want to visit 0th index
            # else it will be counted as a province
            # if s == 0:
            #     continue
            if visited[s] == False:
                self.DFS(s, visited)
                count+=1
        return count

# 0 based indexing
edges = [(0,1),(1,2),(3,4),(4,5),(6,7)]

# # 1 based indexing
# edges = [(1,2),(2,3),(4,5),(5,6),(7,8)]

num_vertices = max(max(edges)) + 1

g = Graph(num_vertices)

for edge in edges:
    g.add_edge(edge[0], edge[1])

#Print the adjacency list before DFS
g.print_graph()

# Perform DFS
print(f"\nNumber of provinces: {g.number_of_provinces()}")