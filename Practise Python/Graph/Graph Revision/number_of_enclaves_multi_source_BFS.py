def bfs(graph, i, j, visited):
    visited[i][j] = True
    queue = []
    queue.append((i, j))
    
    del_row = [-1 , 0 , 1 , 0]
    del_col = [0 , 1 , 0 , -1]
    
    while queue:
        a,b = queue.pop(0)
        for k in range(4):
            neigh_row = a + del_row[k]
            neigh_col = b + del_col[k]
            
            if(
               neigh_row >=0 and neigh_row < len(graph) and
               neigh_col >=0 and neigh_col < len(graph[0]) and
               graph[neigh_row][neigh_col] == 1 and
               visited[neigh_row][neigh_col] == False
               ):
                visited[neigh_row][neigh_col] = True
                queue.append((neigh_row, neigh_col))
               

def number_of_enclaves(graph):
    rows = len(graph)
    cols = len(graph[0])
    visited = [[False] * cols for _ in range(rows)]
    
    # Traverse the first and last row boundary 
    for i in range(cols):
        if graph[0][i] == 1 and visited[0][i] == False:
            bfs(graph, 0, i, visited)
        
        if graph[rows-1][i] == 1 and visited[rows-1][i] == False:
            bfs(graph, rows-1, i, visited)
    
    # Traverse the first and last column boundary
    for j in range(rows):
            if graph[j][0] == 1 and visited[j][0] == False:
                bfs(graph, j, 0, visited)
            
            if graph[j][cols-1] == 1 and visited[j][cols-1] == False:
                bfs(graph, j, cols-1, visited)
    
    count = 0
    # Traverse the rest of the graph to replace 'O' with 'X'
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1 and visited[i][j] == False:
                count += 1
    
    return count


graph = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

print(f"Number of enclaves: {number_of_enclaves(graph)}")