def dfs(graph, i, j, visited):
    visited[i][j] = True
    
    del_row = [-1 , 0 , 1 , 0]
    del_col = [0 , 1 , 0 , -1]
    
    for k in range(4):
        neigh_row = i + del_row[k]
        neigh_col = j + del_col[k]
        
        if (
            neigh_row >= 0 and neigh_row < len(graph) and
            neigh_col >= 0 and neigh_col < len(graph[0]) and
            visited[neigh_row][neigh_col] == False and
            graph[neigh_row][neigh_col] == "O"
        ):
            dfs(graph, neigh_row, neigh_col, visited)


def replace_Os_with_X(graph):
        rows = len(graph)
        cols = len(graph[0])
        visited = [[False] * cols for _ in range(rows)]
        
        # Traverse the first and last row boundary 
        for i in range(cols):
            if graph[0][i] == 'O' and visited[0][i] == False:
                dfs(graph, 0, i, visited)
            
            if graph[rows-1][i] == 'O' and visited[rows-1][i] == False:
                dfs(graph, rows-1, i, visited)
        
        # Traverse the first and last column boundary
        for j in range(rows):
            if graph[j][0] == 'O' and visited[j][0] == False:
                dfs(graph, j, 0, visited)
            
            if graph[j][cols-1] == 'O' and visited[j][cols-1] == False:
                dfs(graph, j, cols-1, visited)
        
        # Traverse the rest of the graph to replace 'O' with 'X'
        for i in range(rows):
            for j in range(cols):
                if graph[i][j] == 'O' and visited[i][j] == False:
                    graph[i][j] = 'X'
        
        # Print the final graph
        for row in graph:
          print(row)



graph = [
       ['X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'O', 'O', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'X', 'O', 'O']
       ]

replace_Os_with_X(graph)