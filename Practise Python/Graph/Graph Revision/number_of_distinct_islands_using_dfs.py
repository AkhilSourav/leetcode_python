def dfs(graph, i, j, visited, island, start):
    visited[i][j] = True
    island.append((i - start[0] , j - start[1]))
    del_row = [-1 , 0 , 1 , 0]
    del_col = [0 , -1 , 0 , 1]
    
    for k in range(4):
        neigh_row = i + del_row[k]
        neigh_col = j + del_col[k]
        
        if(
               0 <= neigh_row < len(graph) and
               0 <= neigh_col < len(graph[0]) and
               graph[neigh_row][neigh_col] and
               visited[neigh_row][neigh_col] == False
          ):
            dfs(graph, neigh_row, neigh_col, visited, island, start)
        

def num_of_distinct_Islands(graph):
    rows = len(graph)
    cols = len(graph[0])
    visited = [[False] * cols for _ in range(rows)]
    my_unique_set = set()
    
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] and not visited[i][j]:
                # We are using list because we want to keep the entire order of the coordinates
                island = []
                start = (i, j)
                dfs(graph, i, j, visited, island, start)
                # We are using set because we want to remove the duplicate islands
                # An island is basically an entire list of coordinates for that island
                # We are converting the list to tuple because set can't take list as an argument
                my_unique_set.add(tuple(island))
    
    print(my_unique_set)
    return len(my_unique_set)


graph = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
]

# graph = [
#             [1, 1, 0, 1, 1],
#             [1, 0, 0, 0, 0],
#             [0, 0, 0, 0, 1],
#             [1, 1, 0, 1, 1],
#         ]


print(f"Number of distinct islands: {num_of_distinct_Islands(graph)}")