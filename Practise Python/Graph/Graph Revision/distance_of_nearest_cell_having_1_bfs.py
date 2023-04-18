def BFS(distance, visited, grid):
    queue = []
    # MultiSource BFS Code 
    # Inserting all the nodes having value 1 in the queue with distance 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                visited[i][j] = True
                queue.append(((i, j), 0))
    
    
    del_row = [-1, 0, 1, 0]
    del_col = [0, 1, 0, -1]
    
    while queue:
        node, dist = queue.pop(0)
        node_i, node_j = node
        distance[node_i][node_j] = dist
        
        for i in range(4):
            neigh_row = node_i + del_row[i]
            neigh_col = node_j + del_col[i]
            
            if (
                neigh_row >=0 and neigh_col>=0 and neigh_row<len(grid) and neigh_col<len(grid[0]) and
                visited[neigh_row][neigh_col] == False and grid[neigh_row][neigh_col] == 0
            ):
                visited[neigh_row][neigh_col] = True
                queue.append(((neigh_row, neigh_col), dist+1))




def get_distance_matrix(grid):
    n = len(grid)
    m = len(grid[0])

    # Create a visited matrix for the grid
    visited = [[False]* m for _ in range(n)]
    distance = [[0]* m for _ in range(n)]

    BFS(distance, visited, grid)
    
    for row in distance:
        print(row)




# Given Grid
grid = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 0]
    ]



""" NOTE : MultiSource BFS"""
get_distance_matrix(grid)