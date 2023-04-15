# Given the lit of edges of a graph, create an adjacency matrix
edges = [(0,1),(0,2),(2,1),(2,3)]

# Get the number of vertices in the graph
num_vertices = max(max(edges)) + 1

# Create an empty adjacency matrix
adj_matrix = [[0] * num_vertices for num in range(num_vertices)]

# Fill in the entries of the adjacency matrix
for edge in edges:
    adj_matrix[edge[0]][edge[1]] = 1
    adj_matrix[edge[1]][edge[0]] = 1

# Print the adjacency matrix
for row in adj_matrix:
    print(row)