def rotten_oranges(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]* m for _ in range(n)]

    queue = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append(((i, j),0))
                visited[i][j] = True
    
    del_row = [-1, 0, 1, 0]
    del_col = [0, 1, 0, -1]
    tm = 0
    while queue:
        curr, t = queue.pop(0)
        x = curr[0]
        y = curr[1]
        tm = max(tm, t)
        
        for i in range(4):
            neigh_row = x + del_row[i]
            neigh_col = y + del_col[i]
            
            if (
                neigh_row >= 0 and neigh_col >= 0 and neigh_row < n and neigh_col < m and
                visited[neigh_row][neigh_col] == False and grid[neigh_row][neigh_col] == 1
            ):
                visited[neigh_row][neigh_col] = True
                grid[neigh_row][neigh_col] = 2
                queue.append(((neigh_row, neigh_col), t+1))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1
    
    return tm



grid = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]
]

# grid = [[2,1,1],[1,1,0],[0,1,1]]

# grid = [[2,1,1],[0,1,1],[1,0,1]]

# grid = [[0,2]]


""" NOTE: In the question it is asked minimum time taken to rot all the oranges
    thats why we are using BFS and not DFS, since BFS traverse all the nodes level wise"""
print(f"Time taken: {rotten_oranges(grid)}")